from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__)
	app.secret_key = 'asdjewmcds1knjk4lknl3lkn1lkn3lkn45lklkm'

	from . import urlshort
	app.register_blueprint(urlshort.bp)

	return app