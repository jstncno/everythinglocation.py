# everythinglocation.py

A wrapper for the everythinglocation API
----------------------------------------

_everythinglocation.py_ is a Pythonic wrapper library for the [everythinglocation](https://www.everythinglocation.com) API. By calling the functions and methods available in _everythinglocation.py_ you can simplify your code and easily access the Address Verification and Geocoding services that **everythinglocation** provides. To learn more about **everythinglocation**, visit their website at [https://www.everythinglocation.com](https://www.everythinglocation.com). **everythinglocation** is a product of [GBG Loqate](http://www.loqate.com).

**NOTE**: _everythinglocation.py_ is still currently in its development stages. This should not be used for production as this branch is unstable and may produce unexpected results.

Features
--------
* Currently able to make Verify requests to the **everythinglocation** API 
* Implemented unit tests to upkeep robustness of code now and throughout the development phases
* Search, Geocode, and more coming soon....

Installation
------------
Installation of _everythinglocation.py_ is currently only available by downloading the [source from GitHub](https://github.com/bumrush/everythinglocation.py) and installing it yourself. There are plans to release this packing to the Python Package Index (PyPI) in the near future.

Usage
-----
#### API Key
In order to use _everythinglocation.py_, you must have an API key. To obtain a key, please visit the [everythinglocation website](https://www.everythinglocation.com) and sign up for an account (your first 100 calls are free).

_everythinglocation.py_ loads your API key from an environment variable called `EVERYTHINGLOCATION_API_KEY`. If no such environment variable exists, you can assign it like so:

```python
>>> import everythinglocation
>>> everythinglocation.API_KEY = 'YOUR_API_KEY_HERE'
```
#### Making calls to **everythinglocation**
The `EverythingLocation()` class takes in a Python dictionary as input to send to the **everythinglocation** service and returns a **ELReponse** object.
```python
>>> import everythinglocation
>>> EL = everythinglocation.EverythingLocation()
>>> print EL.version
2.15.0.7762
>>> params = {'addr': '999 Baker Way San Mateo CA USA'}
>>> response = EL.verify(params)
>>> print response.results[0].AVC
V44-I44-P3-100
>>> print response.results[0].Address1
999 Baker Way
>>> print response.results[0].Address2
San Mateo CA 94404-1578
>>> print response.results[0].CountryName
United States
>>> print response.results[0].ISO3166_2
US
```
For more information about input parameters and output fields, please visit the [everythinglocation REST Transactional Processing Documentation](https://www.everythinglocation.com/api-rest-transactional/).

Future
------
More features and documentation coming soon.