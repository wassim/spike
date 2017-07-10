from twython import Twython, TwythonError
import json
import urllib
import requests
import ssl

# url to our rest api
url = 'https://remotejunior.com/wp-json/wp/v2/job';

# do the request
response = urllib.urlopen(url)

# decode json
data = json.loads(response.read().decode('utf-8'))