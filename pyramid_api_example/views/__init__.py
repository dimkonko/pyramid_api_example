from pyramid.view import view_defaults


class BaseView:

    def __init__(self, request, *args, **kwargs):
        self.request = request


@view_defaults(renderer='json')
class JsonView(BaseView):
    pass
