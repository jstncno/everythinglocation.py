# -*- coding: utf-8 -*-

"""
everythinglocation.base
~~~~~~~~~~~~~~~
This module implements the class that makes calls to the everythinglocation API.

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""
import json, requests, os

from .response import ELResponse

class APIKeyError(Exception):
    pass

class Loqate(object):
    headers = {
        'content-length': '50',
        'keep-alive': 'timeout=1, max=100',
        'connection': 'Keep-Alive',
        'cache-control': 'max-age=0, no-store, no-cache',
        'content-type': 'application/json; charset=utf-8'
    }
    BASE_PATH = ''
    RESOURCES = {}

    def __init__(self):
        self.base_uri = 'https://saas.loqate.com'

    def _get_path(self, key):
        return os.path.join(self.BASE_PATH, self.RESOURCES[key]) if key else self.BASE_PATH

    def _get_complete_url(self, resource):
        return os.path.join(self.base_uri, self._get_path(resource))

    def _get_params(self, params):
        from . import API_KEY
        if not API_KEY:
            raise APIKeyError

        api_dict = {'lqtkey': API_KEY}
        if params:
            params.update(api_dict)
        else:
            params = api_dict
        return params

    def _request(self, method, resource, params=None, **kwargs):
        url = self._get_complete_url(resource)
        params = self._get_params(params)

        response = requests.request(
            method, url, params=params, **kwargs)

        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.json()

    def _GET(self, resource=None, params=None):
        return self._request('GET', resource, params=params)

    def _POST(self, resource, params=None, **kwargs):
        return self._request('POST', resource, params=params, **kwargs)

    '''
    def _DELETE(self, path, params=None, payload=None):
        return self._request('DELETE', path, params=params, payload=payload)
    '''