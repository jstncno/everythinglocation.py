# -*- coding: utf-8 -*-

"""
everythinglocation.response
~~~~~~~~~~~~~~~
This module implements the response classes that are returned by
API calls to everythinglocation.

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import json, requests, pprint
from .address import ELAddress

class BadResponseError(Exception):
    pass

class ELResponse(object):
    '''
    The object returned from calls to the everythinglocation API
    '''
    def __init__(self, response):
        self.body = response
        self.status = response['status']
        if self.status != 'OK':
            raise BadResponseError
        if 'Server' in response:
            if 'Version' in response['Server']:
                self.version = response['Server']['Version']
        if 'session_id' in response:
            self.session_id = response['session_id']
        if 'results' in response:
            self.results = []
            self._build_results(response['results'])

    def _build_results(self, results):
        for result in results:
            self.results.append(ELAddress(result))

    def __str__(self):
        return pprint.pformat(self.body)

class BatchCreateResponse(ELResponse):
    '''
    The Batch response for the Create resource
    '''
    def __init__(self, response):
        super(BatchCreateResponse, self).__init__(response)
        if 'confirmcode' not in response:
            raise BadResponseError
        self.confirm_code = response['confirmcode']

class BatchConfirmResponse(ELResponse):
    '''
    The Batch response for the Confirm resource
    '''
    def __init__(self, response):
        super(BatchConfirmResponse, self).__init__(response)
        try:
            self.batch_status = response['BatchStatus']
            self.batch_id = response['BatchId']
        except:
            raise BadResponseError
