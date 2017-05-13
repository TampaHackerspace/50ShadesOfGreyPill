import geoip2.database
import sys
import json

ip = str(sys.argv[1])
reader = geoip2.database.Reader('GeoLite2-City.mmdb')

response = reader.city(ip)

iso = response.country.iso_code
country = response.country.name
subname = response.subdivisions.most_specific.name
subiso = response.subdivisions.most_specific.iso_code
city = response.city.name
postal = response.postal.code
lat = response.location.latitude
long = response.location.longitude
ipinfo = {ip:{"iso":iso, "country":country,  "subname":subname, "subiso":subiso, "city":city, "postal":postal, "lat":lat, "long":long}}
print (ipinfo)
reader.close()