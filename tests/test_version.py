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
        self.response = requests.get('https://saas.loqate.com/rest/version', self.params)
        self.d = self.response.json()

    def test_response(self):
        '''
        Tests for validity of response
        '''
        assert isinstance(self.d, dict)

    def test_version(self):
        '''
        Tests for valid response status and prints API Version
        '''
        assert 'status' in self.d
        assert self.d['status'] == 'OK'
        assert 'Server' in self.d
        assert 'Version' in self.d['Server']
        print '-' * 70
        print 'Cloud API Version:', self.d['Server']['Version']

    def test_demo(self):
        self.params['p'] = 'v+g'
        self.params['addr'] = '22 caledonia place bristol GBR'
        self.response = requests.get('https://saas.loqate.com/rest', self.params)
        #print self.response.json()
        response = everythinglocation.ELResponse(self.response.json())

if __name__ == '__main__':
    unittest.main()
