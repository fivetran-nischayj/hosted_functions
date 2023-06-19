import calculator
import json
import requests
import numpy

def handle_request(params):
    api_key = params["secrets"]["api_key"]
    url = "https://api.kustomerapp.com/v1/conversations"
    headers = {"Authorization": "Bearer " + api_key}

    # random numpy operation - not used
    arr = numpy.array([3, 2, 1])
    numpy.sort(arr)
    
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

    
