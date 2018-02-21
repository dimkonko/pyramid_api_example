from http import HTTPStatus

from tests import utils
from tests.functional import BaseFunctionalTest
from pyramid_api_example import routes


class HomeFuncTest(BaseFunctionalTest):

    def test_home(self):
        res = self.app.get(routes.INDEX, status=HTTPStatus.OK)
        response_json = utils.parse_json(res.body)

        self.assertIn('msg', response_json)
