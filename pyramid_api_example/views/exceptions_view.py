import logging

import pyramid.httpexceptions as exc

from pyramid.view import exception_view_config


@exception_view_config(Exception)
def failed_validation(exception, request):
    logging.error(exception, exc_info=True)
    raise exc.HTTPInternalServerError()
