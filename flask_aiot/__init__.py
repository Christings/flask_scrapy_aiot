from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
# from flask.ext.mongoengine import MongoEngine
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.debug = False

app.config["MONGODB_SETTINGS"] = {'DB': "imdb"}
app.config['SECRET_KEY'] = '\x1d\x81\xc6\xa4C\xd7}\x9f\x85=\xab\x1f\x96i\xef\x94\xe4\xc4CQ\xdfz\xf0\\\x1d\x81\xc6\xa4C\xd7}\x9f\x85=\xab\x1f\x96i\xef\x94\xe4\xc4CQ\xdfz\xf0\\'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

# defining the mongoeninge orm
db = MongoEngine(app)


def register_blueprints(app):
    # prevents circular imports
    from flask_imdb.views import movies

    # in case more than one application working with movies exists
    # define url_prefix for each of them, e.g. url_prefix="/imdb"
    app.register_blueprint(movies)

register_blueprints(app)

if __name__ == '__main__':
    app.run()