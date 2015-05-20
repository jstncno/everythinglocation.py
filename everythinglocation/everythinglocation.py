# -*- coding: utf-8 -*-

"""
everythinglocation.everythinglocation
~~~~~~~~~~~~~~~
This module implements the class that makes calls to the everythinglocation API.

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""
import json, requests, os

from .base import Loqate
from .response import ELResponse

class APIKeyError(Exception):
    pass

class EverythingLocation(Loqate):
    BASE_PATH = 'rest'
    RESOURCES = {
        'version': 'version'
    }

    def __init__(self):
        super(EverythingLocation, self).__init__()
        self.response = ELResponse(self._GET(resource='version'))
        self.version = self.response.version

    def verify(self, params, geocode=False):
        params['p'] = 'v'
        if geocode:
            params['p'] += '+g'
        return ELResponse(self._GET(params=params))

