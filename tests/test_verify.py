# -*- coding: utf-8 -*-

"""
everythinglocation.base
~~~~~~~~~~~~~~~
This unittest module tests the everythinglocation Verify Process

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import requests
import unittest
import json

import everythinglocation

class TestVerify(unittest.TestCase):
    '''
    This unittest module tests the everythinglocation Verify Process
    '''
    def setUp(self):
        '''
        Basic setup
        '''
        self.EL = everythinglocation.EverythingLocation()

    def test_verify(self):
        '''
        Tests for valid response from the Verify Process
        '''
        params = {'addr': '22 caledonia place bristol GBR'}
        result = self.EL.verify(params)
        assert len(result.results) > 0
        assert 'V44' in result.results[0].AVC

        params['addr'] = '999 Baker Way San Mateo CA USA'
        result = self.EL.verify(params)
        assert len(result.results) > 0
        assert 'V44' in result.results[0].AVC
        print
        print result.results[0].AVC
        print result.results[0].Address1
        print result.results[0].Address2
        print result.results[0].CountryName
        assert 'United States' == result.results[0].CountryName
        assert 'US' == result.results[0].ISO3166_2


if __name__ == '__main__':
    unittest.main()
