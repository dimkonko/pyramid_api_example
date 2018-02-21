from pyramid_api_example.models import JsonModel


class UserPassword(JsonModel):

    def __init__(self, user_sid, password):
        self.user_sid = user_sid
        self.password = password
