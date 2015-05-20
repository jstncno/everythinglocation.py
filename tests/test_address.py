# -*- coding: utf-8 -*-

"""
test_address
~~~~~~~~~~~~~~~
This unittest module tests the ELAddress class

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import vcr
import requests
import unittest

import everythinglocation

class TestAddress(unittest.TestCase):
    '''
    This unittest module tests the ELAddress class
    '''
    @vcr.use_cassette('tests/cassettes/setup.yaml')
    def setUp(self):
        '''
        Basic setup
        '''
        self.EL = everythinglocation.EverythingLocation()

    @vcr.use_cassette('tests/cassettes/address.yaml')
    def test_address(self):
        '''
        Tests ELAddress for validity
        '''
        params = {'addr': '999 Baker Way San Mateo CA USA'}
        result = self.EL.verify(params)
        assert len(result.results) > 0
        print result.results[0].fields


if __name__ == '__main__':
    unittest.main()
