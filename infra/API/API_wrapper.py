import json
import os

import requests
from os.path import dirname as up
# try:
#     with open('../../config.json') as f:
#         data_config = json.load(f)
# except FileNotFoundError:
#     print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
#     raise  # Raise the error to halt execution if the file is essential for the script to run


class APIWrapper:
    def __init__(self):
        self.response = None
        self.myrequest = requests
        cur_dir = up(up(up(os.path.abspath(__file__))))
        config_location = os.path.join(cur_dir,'config.json')
        with open(config_location) as f:
            self.data_config = json.load(f)

    def api_get_request(self, url):
        self.response = self.myrequest.get(url, headers={"Authorization": self.data_config["Authorization"]})
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_get_request_by_id(self, url, id):
        self.response = self.myrequest.get(url+id, headers={"Authorization": self.data_config["Authorization"]})
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_get_request_with_params(self, url, params):
        self.response = self.myrequest.get(url, params=params, headers={"Authorization": self.data_config["Authorization"]})
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def make_post_request(self, url, data=None):
        self.response = self.myrequest.post(url, json=data, headers={"Authorization": self.data_config["Authorization"]})
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def make_post_request_with_id(self, url, id, data=None):
        self.response = self.myrequest.post(url+id, json=data, headers={"Authorization": self.data_config["Authorization"]})
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def make_put_request(self, url, data=None):
        self.response = self.myrequest.put(url, json=data, headers={"Authorization": self.data_config["Authorization"]})
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def make_patch_request(self, url, data=None):
        self.response = self.myrequest.patch(url, json=data, headers={"Authorization": self.data_config["Authorization"]})
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def make_delete_request(self, url, id):
        self.response = self.myrequest.delete(url+id, headers={"Authorization": self.data_config["Authorization"]})
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code
