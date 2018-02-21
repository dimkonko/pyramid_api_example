import os

SERVER_APP_ROOT_PATH = os.path.join(os.path.dirname(__file__))

SERVER_ROOT_PATH = os.path.join(SERVER_APP_ROOT_PATH, '..')
STATIC_ROOT_PATH = os.path.join(SERVER_APP_ROOT_PATH, '../client')
INDEX_HTML_PATH = os.path.join(STATIC_ROOT_PATH, 'index.html')
FIXTURES_PATH = os.path.join(SERVER_APP_ROOT_PATH, 'fixtures')
