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
        self.auth = everythinglocation.ELAuth{}

    @vcr.use_cassette('tests/cassettes/auth.yaml')
    def test_auth(self):
        '''
        Tests ELAuth for validity
        '''
        params = {'addr': '999 Baker Way San Mateo CA USA'}
        result = self.auth.verify(params)
        assert len(result.results) > 0
        print
        print result.results[0].fields
        print '-' * 70


if __name__ == '__main__':
    unittest.main()
