from pyramid.view import view_config

from pyramid_api_example import routes
from pyramid_api_example.views import JsonView


class IndexView(JsonView):

    @view_config(route_name=routes.INDEX, request_method='GET')
    def home(self):
        return {'msg': 'hello'}
