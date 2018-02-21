from pyramid_api_example.persister import user_persister


def _get_persister():
    return user_persister.FixtureUserPersister()


def get_user(user_sid):
    persister = _get_persister()
    return persister.fetch_single(user_sid)
