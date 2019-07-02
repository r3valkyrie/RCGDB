import json


class LoadConfig:
    def __init__(self):
        with open('config.json') as config:
            c_data = json.load(config)
            self.token = c_data['token']
            self.role_whitelist = c_data['role_whitelist']