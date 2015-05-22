# -*- coding: utf-8 -*-

"""
everythinglocation.batch
~~~~~~~~~~~~~~~
This module implements the class that makes batch processing calls to the
everythinglocation API.

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from .base import Loqate
from .everythinglocation import EverythingLocation
from .response import ELResponse

class InvalidCredentialsError(Exception):
    pass

class Batch(Loqate):
    BASE_PATH = 'batch'
    RESOURCES = {
        'create': 'create.php'
    }

    def __init__(self):
        super(Batch, self).__init__()

    def create(self, params):
        params
        return self._process(params)

    def search(self, params, geocode=False):
        params['p'] = 's'
        if geocode:
            params['p'] += '+g'
        return self._process(params)

    def _process(self, params):
        return ELResponse(self._GET(params=params))

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