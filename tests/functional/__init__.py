import os
import unittest

from pyramid import testing
from pyramid.paster import get_appsettings
from webtest import TestApp

from pyramid_api_example import main
from pyramid_api_example.path import SERVER_ROOT_PATH

app_settings = get_appsettings(
    config_uri=os.path.join(SERVER_ROOT_PATH, 'etc', 'local.ini'))
app = main({}, **app_settings)


class BaseFunctionalTest(unittest.TestCase):

    def setUp(self):
        testing.setUp()

        self.app = TestApp(app)

    def tearDown(self):
        testing.tearDown()
