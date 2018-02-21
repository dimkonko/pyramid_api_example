import os
import json

from pyramid_api_example import path


class LivePersister:

    def _execute(self, query, params):
        return


class FixturePersister:

    def _load_fixture_json(self, fixture_file_path):
        """

        :param fixture_file_path:
        :return dict:
        """
        fixture_path = os.path.join(path.FIXTURES_PATH, fixture_file_path)

        with open(fixture_path, 'r') as fixture_json_file:
            fixture_json = json.load(fixture_json_file)

        return fixture_json
