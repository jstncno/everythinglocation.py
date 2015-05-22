# -*- coding: utf-8 -*-

"""
test_batch
~~~~~~~~~~~~~~~
This unittest module tests the Batch class

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import vcr
import requests
import unittest

import everythinglocation

class TestBatch(unittest.TestCase):
    '''
    This unittest module tests the Batch class
    '''
    @vcr.use_cassette('tests/cassettes/batch_setup.yaml')
    def setUp(self):
        '''
        Basic setup
        '''
        self.batch = everythinglocation.Batch()

    @vcr.use_cassette('tests/cassettes/batch.yaml')
    def test_create(self):
        '''
        Tests Batch().create()
        '''
        params = {
            'lqt_file': 'lqt-batch-file-template.txt',
            'transactiontype': 'V',
            'name': 'test_batch_upload',
            'optiondefaultcountry': 'USA'
        }

        r = self.batch.create(params)
        assert r.status == 'OK'


if __name__ == '__main__':
    unittest.main()
