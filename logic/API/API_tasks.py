import json

try:
    with open('../../config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run


class Tasks:
    def __init__(self, api_ob):
        self.my_api = api_ob


    def get_active_tasks(self):
        res = self.my_api.api_get_request(data["url_tasks_api"])
        return res

    def create_tasks(self, body):
        res = self.my_api.make_post_request(data["url_tasks_api"], body)
        return res

    def update_tasks(self, name, body):
        name_to_send = f"?content={name}"
        res = self.my_api.make_post_request_with_id(data["url_tasks_api"], name_to_send, body)
        return res

    def delete_tasks(self, name):
        name_to_send = f"?content={name}"
        res = self.my_api.make_delete_request(data["url_tasks_api"], name_to_send)
        return res




