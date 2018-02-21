import abc

from pyramid_api_example.models.user_password import UserPassword
from pyramid_api_example.persister import LivePersister, FixturePersister


USER_PERSISTER = FixturePersister()

USER_SID = "user_sid"
PASSWORD = "password"


class UserPasswordPersister(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fetch_single(self, user_uid):
        pass

    @abc.abstractmethod
    def fetch_multiple(self, user_uids):
        pass

    def create_user_password(self, row):
        user_passwd = UserPassword(
            row[USER_SID],
            row[PASSWORD])

        return user_passwd


class LiveUserPasswordPersister(UserPasswordPersister, LivePersister):

    def fetch_single(self, user_uid):
        pass

    def fetch_multiple(self, user_uids):
        pass


class FixtureUserPasswordPersister(UserPasswordPersister, FixturePersister):

    FIXTURE_FILE_PATH = "user_passwords.json"

    def fetch_single(self, user_uid):
        fixture_json = self._load_fixture_json(self.FIXTURE_FILE_PATH)

        user_passwd = None

        obj = fixture_json.get(user_uid)
        if obj is not None:
            user_passwd = self.create_user_password(obj)

        return user_passwd

    def fetch_multiple(self, user_uids):
        fixture_json = self._load_fixture_json(self.FIXTURE_FILE_PATH)

        user_passwds = []
        for user_uid in user_uids:
            obj = fixture_json.get(user_uid)
            if obj is not None:
                user_passwds.append(self.create_user_password(obj))

        return user_passwds
