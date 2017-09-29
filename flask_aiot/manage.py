#!/usr/bin/env python
import os
# from app import create_app, db
from app import create_app, mongo
from app.models import User, AllProductPrice, Ny135, Chinacwa, Iot
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# from app.models import Movies

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, mongo)


def make_shell_context():
    return dict(app=app, db=mongo, User=User, AllProductPrice=AllProductPrice,
                Ny135=Ny135, Chinacwa=Chinacwa, Iot=Iot)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
