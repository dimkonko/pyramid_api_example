import pyramid.httpexceptions as exc

from pyramid.view import view_config

from pyramid_api_example import routes
from pyramid_api_example.constants import json_keys
from pyramid_api_example.services import user_service
from pyramid_api_example.views import JsonView


class UserResourceController(JsonView):

    @view_config(route_name=routes.USERS, request_method='GET')
    def get_all(self):
        pass

    @view_config(route_name=routes.USER, request_method='GET')
    def get_single(self):
        user_sid = self.request.matchdict[json_keys.USER_SID]

        user = user_service.get_user(user_sid)
        if user is None:
            raise exc.HTTPNotFound()

        j = user.to_json()
        return j
