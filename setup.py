# -*- coding: utf-8 -*-

# See http://pythonhosted.org/an_example_pypi_project/setuptools.html

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Install requests==2.5.3 to avoid InsecurePlatformWarning message
# http://stackoverflow.com/questions/29134512/insecureplatformwarning-a-true-sslcontext-object-is-not-available-this-prevent
# https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning
setup(
    name = 'everythinglocation',
    version = '0.0.1',
    author = 'Justin Cano',
    author_email = 'jcano001@ucr.edu',
    description = 'A Python wrapper for everythinglocation API',
    keywords = ['everythinglocation', 'address', 'verification', 'geocoding'
                'address verification', 'loqate' 'gbg', 'gbg loqate'],
    url = 'https://github.com/earthican/everythinglocation.py',
    download_url = 'https://github.com/earthican/everythinglocation.py/archive/master.zip',
    packages = ['everythinglocation'],
    long_description=read('README.md'),
    install_requires = ['requests==2.5.3'],
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities"
    ],
)
