# -*- coding: utf-8 -*-

"""
everythinglocation.response
~~~~~~~~~~~~~~~
This module implements the response class that is returned by
API calls to everythinglocation.

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import json, requests
from .address import ELAddress

class BadResponseError(Exception):
    pass

class ELResponse(object):
    '''
    The object returned from calls to the everythinglocation API
    '''
    def __init__(self, response):
        self.status = response['status']
        if self.status != 'OK':
            raise BadResponseError
        if 'Server' in response:
            if 'Version' in response['Server']:
                self.version = response['Server']['Version']
        if 'results' in response:
            self.results = []
            self._build_results(response['results'])

    def _build_results(self, results):
        for result in results:
            self.results.append(ELAddress(result))
