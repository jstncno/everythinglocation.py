# -*- coding: utf-8 -*-

"""
test_auth
~~~~~~~~~~~~~~~
This unittest module tests the ELAuth class

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import vcr
import requests
import unittest
import os

import everythinglocation

class TestAuth(unittest.TestCase):
    '''
    This unittest module tests the ELAuth class
    '''
    @vcr.use_cassette('tests/cassettes/auth_setup.yaml')
    def setUp(self):
        '''
        Basic setup
        '''
        self.EL = everythinglocation.EverythingLocation()
        username = os.environ['EVERYTHINGLOCATION_USERNAME']
        password = os.environ['EVERYTHINGLOCATION_PASSWORD']
        auth = {
            'username': username,
            'password': password
        }
        self.auth_session_1 = self.EL.authorize(auth)
        self.auth_session_2 = self.EL.authorize(username=username, password=password)

    @vcr.use_cassette('tests/cassettes/auth.yaml')
    def test_auth(self):
        '''
        Tests ELAuth for validity
        '''
        assert 'session_id' in self.auth_session_1.body
        assert 'session_id' in self.auth_session_2.body

if __name__ == '__main__':
    unittest.main()
