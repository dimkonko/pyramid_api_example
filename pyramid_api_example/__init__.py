from pyramid.config import Configurator

from pyramid_api_example import routes


def main(global_config, **settings):
    config = Configurator(settings=settings)

    add_routes(config)

    config.scan()
    return config.make_wsgi_app()


def add_routes(config):
    for url in routes.ROUTES:
        config.add_route(url, url)
