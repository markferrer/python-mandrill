import simplejson as json
import requests


class API(object):  
    
    def __init__(self, api_key):
        self.api_url = 'https://mandrillapp.com/api/1.0/'

    def _method_url(self, method, data_type='json')
        return self.api_url + method + '.' + data_type

    def _api_response(self, response):
        """
        Converts the json response into python data types.
        """
        json_response = json.loads(response.text)
        json_response['status_code'] = response.status_code
        return json_response

    def post(self, method_name, payload):
        url = self._method_url(method_name)

        json_data = json.dumps(payload)
        headers = {
            'content-type': 'application/json'
        }

        post_response = requests.post(url, data=json_data, headers=headers)
        decoded_response = self._api_response(post_response)
        return decoded_response
