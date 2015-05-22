# -*- coding: utf-8 -*-

"""
everythinglocation.batch
~~~~~~~~~~~~~~~
This module implements the class that makes batch processing calls to the
everythinglocation API.

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""
import requests, os
from requests_toolbelt.multipart.encoder import MultipartEncoder

from .base import Loqate
from .everythinglocation import EverythingLocation
from .response import BatchResponse

class MissingRequiredParameters(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

class Batch(Loqate):
    BASE_PATH = 'batch'
    RESOURCES = {
        'create': 'create.php'
    }

    def __init__(self):
        super(Batch, self).__init__()
        self.jobs = {} # store jobs as dict with key == BatchResponse.confirm_code

    def _get_params(self, params):
        super(Batch, self)._get_params(params)
        try:
            assert 'name' in params.keys()
            assert 'optiondefaultcountry' in params.keys()
            assert 'lqt_file' in params.keys()
        except:
            raise MissingRequiredParameters
        return params

    def create(self, params, auto=False):
        params = self._get_params(params)
        file_path = os.path.abspath(params['lqt_file'])
        encoder = MultipartEncoder(
            fields={'lqt_file': (params['lqt_file'], open(file_path, 'rb'), 'text/plain')}
        )
        headers = {
            'Content-Type': encoder.content_type
        }

        response = self._post('create', params , data=encoder, headers=headers)
        self.jobs[response.confirm_code] = response

        # TODOD: if auto, then confirm job
        # if auto:
        #   self.confirm(response.confirm_code)

        return response

    def _post(self, resource, params, **kwargs):
        return BatchResponse(self._POST(resource, params=params, **kwargs))

class ELAuth(object):
    def __init__(self, auth=None, **kwargs):
        EL = EverythingLocation()
        try:
            if not auth:
                assert 'username' in kwargs.keys()
                assert 'password' in kwargs.keys()
                for key, value in kwargs.iteritems():
                    auth[key] = value
            else:
                assert isinstance(auth, dict)
                assert 'username' in auth.keys()
                assert 'password' in auth.keys()
        except:
            raise InvalidCredentialsError

        auth_session = EL.authorize(auth)
        self.session_id = auth_response.session_id