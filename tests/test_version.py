# -*- coding: utf-8 -*-

"""
everythinglocation.base
~~~~~~~~~~~~~~~
This unittest module tests the response for the Cloud API Version

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import vcr
import requests
import unittest

import everythinglocation

class TestVersion(unittest.TestCase):
    '''
    This unittest module tests the response for the Cloud API Version
    '''
    #@vcr.use_cassette('tests/cassettes/version.yaml')
    def setUp(self):
        '''
        Basic setup
        '''
        self.EL = everythinglocation.EverythingLocation()
        self.params = self.EL._get_params({})
        self.response = requests.get('https://saas.loqate.com/rest/version', params=self.params)
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
        print
        print '-' * 70
        print 'Cloud API Version:', self.d['Server']['Version']
        print self.EL.version

if __name__ == '__main__':
    unittest.main()
