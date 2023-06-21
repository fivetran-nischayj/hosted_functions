import calculator
import json
import requests

def handle_request(params):
    api_key = params["secrets"]["api_key"]
    url = "https://api.kustomerapp.com/v1/conversations"
    headers = {"Authorization": "Bearer " + api_key}

    # check module function
    result = calculator.add(2, 3)
    
    response = requests.get(url=url, headers=headers)
    conversations = json.loads(response.text)['data']
    return {
      'state': {},
      'insert': {
        'conversation': conversations
      },
      'schema': {
        'conversation': {
          'primary_key': ['id']
        }
      }
    }

    
