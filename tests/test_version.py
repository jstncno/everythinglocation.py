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

    def test_version(self):
        pass

if __name__ == '__main__':
    unittest.main()