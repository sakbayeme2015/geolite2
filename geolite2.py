download GeoLite2-City.mmdb
pip install geoip2 



>>> import geoip2.database
>>> reader = geoip2.database.Reader('GeoLite2-City.mmdb')
>>> response = reader.city('2.11.231.234')
>>> response.country.iso_code
u'FR'
>>> response.city.name
u'Issy-les-Moulineaux'
>>> response.postal.code
u'92130'
>>> response.location.latitude
48.821
>>> response.location.longitude
2.2772

