import base64
import requests
import re

# twitter API credentials
client_key = 'pPddUqddPR5TrHMa23qxYnUb3'
client_secret = 'hp1oz8W6Kq5GWt5oQBCnLe83mwImyWO2E4rp1sQQCateZzc8C3'

# encoding client key and secret key
key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

# creating request url for API authorisation token
base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

# authorisation headers for API request
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

# data type client credentials
auth_data = {
    'grant_type': 'client_credentials'
}

# getting access token with POST request to the API
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
access_token = auth_resp.json()['access_token']

# search headers with the authorised access token
search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

# function that performs the API request and returns top 10 results for the given country (woeid)
def tt(woeid, rgx):
    search_url = 'https://api.twitter.com/1.1/trends/place.json?id={}'.format(woeid)
    r0 = requests.get(search_url, headers=search_headers)
    data = r0.text
    m1 = re.findall(rgx, data)
    return m1[:10]