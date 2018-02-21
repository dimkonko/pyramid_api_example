from pyramid_api_example.constants import json_keys
from pyramid_api_example.models import JsonModel


class User(JsonModel):

    def __init__(self, user_sid, first_name, last_name, email, dob):
        self.user_sid = user_sid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.dob = dob

    def to_json(self):
        return {
            json_keys.USER_SID: self.user_sid,
            json_keys.FIRST_NAME: self.first_name,
            json_keys.LAST_NAME: self.last_name,
            json_keys.EMAIL: self.email,
            json_keys.DOB: self.dob
        }
