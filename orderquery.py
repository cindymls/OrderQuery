import json
import os
import requests

def get_status(external_id):
  token_url = 'https://api.lulu.com/auth/realms/glasstree/protocol/openid-connect/token'
  client_key = os.environ['client_key'] 
  client_secret = os.environ['client_secret']
  data = {'grant_type': 'client_credentials'}
  access_token_response = requests.post(token_url,  data=data,verify=False,allow_redirects=False,auth=(client_key, client_secret))
  tokens = json.loads(access_token_response.text)
  url = 'https://api.lulu.com/print-jobs/'
  headers = { 
    'Cache-Control': 'no-cache',
    'Authorization': 'Bearer '+ tokens['access_token'], 
  }
  response = requests.request('GET',url,headers=headers)
  data = json.loads(response.text)
  for item in data['results']:
    for line in item['line_items']:
      if line['external_id'] == external_id:
        message = {"Order Number": external_id,
                   "Order Status": item['status']['name'], 
                   "Tracking ID": str(line['tracking_id']),
                   "Tracking URL": str(line['tracking_urls'])}
  return(message)




