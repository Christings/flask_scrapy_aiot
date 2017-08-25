import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from flask.ext.script import Manager, Server
from flask_script import Manager,Server
from flask_imdb import app
# from mongoengine.base import ValidationError

# creating an instance of flask-script Manager that will take care of
# all the commands and will handle how they are called from command line
manager = Manager(app)

# customizing and adding the predefined Server command to the manager
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    # host = '0.0.0.0')
    host = '127.0.0.1')
)

if __name__ == "__main__":
    manager.run()