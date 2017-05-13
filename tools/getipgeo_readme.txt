getipgeo.py uses the open source database from GeoLite2-City.mmdb aquired from MaxMind.

Method to use is  getipgeo.py <ipaddress>

Example:
getipgeo.py 76.85.200.64

Result:
{'76.85.200.64': {'iso': 'US', 'country': 'United States', 'lat': 40.8602, 'long': -96.6061, 'subname': 'Nebraska', 'subiso': 'NE', 'postal': '68507', 'city': 'Lincoln'}}
