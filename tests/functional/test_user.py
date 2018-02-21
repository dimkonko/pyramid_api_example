from http import HTTPStatus

from tests import utils
from tests.functional import BaseFunctionalTest
from pyramid_api_example import routes
from pyramid_api_example.constants import json_keys


class UserFuncTest(BaseFunctionalTest):

    def test_get_user(self):
        expected_user_sid = 1

        url = routes.USER.format(user_sid=expected_user_sid)
        res = self.app.get(url, status=HTTPStatus.OK)
        response_json = utils.parse_json(res.body)

        self.assertEqual(expected_user_sid, response_json[json_keys.USER_SID])
