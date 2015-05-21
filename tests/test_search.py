# -*- coding: utf-8 -*-

"""
test_search
~~~~~~~~~~~~~~~
This unittest module tests the everythinglocation Search Process

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import vcr
import requests
import unittest

import everythinglocation

class TestSearch(unittest.TestCase):
    '''
    This unittest module tests the everythinglocation Search Process
    '''
    @vcr.use_cassette('tests/cassettes/setup.yaml')
    def setUp(self):
        '''
        Basic setup
        '''
        self.EL = everythinglocation.EverythingLocation()

    @vcr.use_cassette('tests/cassettes/search.yaml')
    def test_search(self):
        '''
        Tests for valid response from the Verify Process
        '''
        params = {'addr': '999 Baker Way San Mateo CA USA'}
        result = self.EL.search(params)
        assert len(result.results) > 0
        print
        print '-' * 70
        print '# results:', len(result.results)
        print result.results[0]

if __name__ == '__main__':
    unittest.main()
