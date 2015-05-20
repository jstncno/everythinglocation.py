# -*- coding: utf-8 -*-

"""
everythinglocation
~~~~~~~~~~
*everythinglocation* is a wrapper, written in Python, for the everythinglocation
API provided by GBG Loqate. By calling the functions available in *everything*
you can simplify your code and easily make calls to the everythinglocation
service. To find out more about everythinglocation, check out the web page
https://www.everythinglocation.com and documentation page
https://www.everythinglocation.com/api-rest-transactional.

:copyright: (c) 2015 by Justin Cano.
:license: MIT, see LICENSE for more details
"""

__title__ = 'everythinglocation'
__version__ = '0.0.1'
__author__ = 'Justin Cano'
__copyright__ = 'Copyright (c) 2015 Justin Cano'
__license__ = 'MIT'

import os

from .everythinglocation import EverythingLocation
from .response import ELResponse

def _get_env_key(key):
    try:
        return os.environ[key]
    except KeyError:
        return None

API_KEY = _get_env_key('EVERYTHINGLOCATION_API_KEY')