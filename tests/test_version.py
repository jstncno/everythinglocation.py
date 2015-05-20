# -*- coding: utf-8 -*-

"""
test_version
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
    @vcr.use_cassette('tests/cassettes/version.yaml')
    def setUp(self):
        '''
        Basic setup
        '''
        self.EL = everythinglocation.EverythingLocation()
        self.response = self.EL.response

    def test_version(self):
        '''
        Tests for valid response status and prints API Version
        '''
        assert 'status' in self.response.body
        assert self.response.body['status'] == 'OK'
        assert 'Server' in self.response.body
        assert 'Version' in self.response.body['Server']
        print
        print '-' * 70
        assert self.response.body['Server']['Version'] == self.EL.version
        print 'Cloud API Version:', self.EL.version

if __name__ == '__main__':
    unittest.main()
