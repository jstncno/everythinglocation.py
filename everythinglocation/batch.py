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

from .base import Loqate, ELAuth
from .everythinglocation import EverythingLocation
from .response import BatchConfirmResponse, BatchCreateResponse

class MissingRequiredParameters(Exception):
    pass

class Batch(Loqate):
    BASE_PATH = 'batch'
    RESOURCES = {
        'create': 'create.php',
        'confirm': 'confirm.php'
    }

    def __init__(self):
        super(Batch, self).__init__()
        self.job_queue = {} # store pending jobs (BatchCreateResponse) as dict with key == BatchCreateResponse.confirm_code
        self.jobs = {} # store processing jobs (BatchConfirmResponse) as dict with key == BatchConfirmResponse.batch_id

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
        response = BatchCreateResponse(self._POST('create', params , data=encoder, headers=headers))
        self.job_queue[response.confirm_code] = response

        if auto:
            params['confirmcode'] = response.confirm_code
            if 'hasheaderline' not in params.keys():
                params['hasheaderline'] = True
            self.confirm(params)

        return response

    def confirm(self, params):
        params = self._try_confirm_params(params)
        self.job_queue.pop(params['confirmcode'], None)
        response = BatchConfirmResponse(self._GET('confirm', params))
        self.jobs[response.batch_id] = response
        print response.body
        return response


