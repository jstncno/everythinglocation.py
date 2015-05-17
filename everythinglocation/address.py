# -*- coding: utf-8 -*-

"""
everythinglocation.address
~~~~~~~~~~~~~~~
This module implements the address class that is returned by
API calls to everythinglocation.

:copyright: (c) 2015 by Justin Cano
:license: MIT, see LICENSE for more details
"""

import pprint

class ELAddress(object):
    '''
    The Address class
    '''
    def __init__(self, result):
        self._set_attrs_to_values(result)

    def _set_attrs_to_values(self, response={}):
        '''
        Set dictionary values to class attributes
        '''
        if isinstance(response, dict):
            for key in response.keys():
                setattr(self, key, response[key])
