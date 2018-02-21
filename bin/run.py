import os

from pyramid.scripts.pserve import PServeCommand


ini_file = os.path.join(os.path.dirname(__file__), '..', 'etc', 'local.ini')
PServeCommand(['pserve', ini_file]).run()
