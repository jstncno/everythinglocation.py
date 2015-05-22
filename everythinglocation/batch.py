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
from .response import ELResponse, BatchResponse

class MissingRequiredParameters(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

class Batch(Loqate):
    BASE_PATH = 'batch'
    RESOURCES = {
        'create': 'create.php',
        'confirm': 'confirm.php'
    }

    def __init__(self):
        super(Batch, self).__init__()
        self.jobs = {} # store jobs as dict with key == BatchResponse.confirm_code

    def _try_create_params(self, params):
        super(Batch, self)._get_params(params)
        try:
            assert 'name' in params.keys()
            assert 'optiondefaultcountry' in params.keys()
            assert 'lqt_file' in params.keys()
            assert 'transactiontype' in params.keys()
        except:
            raise MissingRequiredParameters
        return params

    def _try_confirm_params(self, params):
        super(Batch, self)._get_params(params)
        try:
            assert 'name' in params.keys()
            assert 'confirmcode' in params.keys()
            assert 'hasheaderline' in params.keys()
            assert 'transactiontype' in params.keys()
        except:
            raise MissingRequiredParameters
        return params

    def create(self, params, auto=False):
        params = self._try_create_params(params)
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
        if auto:
            params['confirmcode'] = response.confirm_code
            params['hasheaderline'] = False
            self.confirm(params)

        return response

    def confirm(self, params):
        params = self._try_confirm_params(params)
        self.jobs.pop(params['confirmcode'], None)
        return self._process('confirm', params)

    def _post(self, resource, params, **kwargs):
        return BatchResponse(self._POST(resource, params=params, **kwargs))

    def _process(self, resource, params):
        return ELResponse(self._GET(params=params, resource=resource))

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