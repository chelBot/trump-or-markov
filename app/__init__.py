from flask import Flask
from settings import APP_PROD
app = Flask(__name__)

class WebFactionMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = '/trump/'
        return self.app(environ, start_response)

if APP_PROD:
    app.wsgi_app = WebFactionMiddleware(app.wsgi_app)

from app import views

if __name__ == '__main__':
    app.run()
