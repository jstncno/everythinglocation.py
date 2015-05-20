# -*- coding: utf-8 -*-

"""
test_geocode
~~~~~~~~~~~~~~~
This unittest module tests the everythinglocation Geocode process

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import vcr
import requests
import unittest

import everythinglocation

class TestGeocode(unittest.TestCase):
    '''
    This unittest module tests the everythinglocation Geocode process
    '''
    @vcr.use_cassette('tests/cassettes/setup.yaml')
    def setUp(self):
        '''
        Basic setup
        '''
        self.EL = everythinglocation.EverythingLocation()

    @vcr.use_cassette('tests/cassettes/geocode.yaml')
    def test_geocode(self):
        '''
        Tests ELAddress for validity
        '''
        params = {'addr': '999 Baker Way San Mateo CA USA'}
        response = self.EL.verify(params, geocode=True)
        assert len(response.results) > 0
        result = response.results[0]
        fields = result.fields
        print
        assert 'GeoAccuracy' in fields
        print   'GeoAccuracy:', result.GeoAccuracy
        assert 'Latitude' in fields
        print   'Latitude:', result.Latitude
        assert 'Longitude' in fields
        print   'Longitude:', result.Longitude
        assert 'GeoDistance' in fields
        print   'GeoDistance:', result.GeoDistance
        print '-' * 70

if __name__ == '__main__':
    unittest.main()
