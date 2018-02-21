import abc

from pyramid_api_example.models.user import User
from pyramid_api_example.persister import LivePersister, FixturePersister


USER_SID = "user_sid"
FIRST_NAME = "first_name"
LAST_NAME = "last_name"
EMAIL = "email"
DOB = "dob"


class UserPersister(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fetch_single(self, user_uid):
        pass

    def create_entity(self, row):
        entity = User(
            row[USER_SID],
            row[FIRST_NAME],
            row[LAST_NAME],
            row[EMAIL],
            row[DOB])

        return entity


class LiveUserPersister(UserPersister, LivePersister):

    def fetch_single(self, user_uid):
        pass


class FixtureUserPersister(UserPersister, FixturePersister):

    FIXTURE_FILE_PATH = "users.json"

    def fetch_single(self, user_uid):
        fixture_json = self._load_fixture_json(self.FIXTURE_FILE_PATH)

        entity = None

        obj = fixture_json.get(user_uid)
        if obj is not None:
            entity = self.create_entity(obj)

        return entity

    # def fetch_users(self, user_uids):
    #     fixture_json = self._load_fixture_json(self.FIXTURE_FILE_PATH)
    #
    #     users = []
    #     for user_uid in user_uids:
    #         user_obj = fixture_json.get(user_uid)
    #         if user_obj is not None:
    #             users.append(self.create_user(user_obj))
    #
    #     return users
