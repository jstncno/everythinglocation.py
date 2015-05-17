# -*- coding: utf-8 -*-

"""
everythinglocation.base
~~~~~~~~~~~~~~~
This unittest module tests the response for the Cloud API Version

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import requests
import unittest
import json
import ast

import everythinglocation

class TestVersion(unittest.TestCase):
    '''
    This unittest module tests the response for the Cloud API Version
    '''
    def setUp(self):
        '''
        Basic setup
        '''
        self.EL = everythinglocation.EverythingLocation()
        self.params = self.EL._get_params({})
        self.URL = self.EL.BASE_PATH

    def test_version(self):
        r = requests.get(self.URL, self.params)
        d = ast.literal_eval(r.text)
        assert('status' in d)
        assert(d['status'] == 'OK')
        assert('Server' in d)
        assert('Version' in d['Server'])
        print '-' * 70
        print 'Cloud API Version:', d['Server']['Version']

if __name__ == '__main__':
    unittest.main()