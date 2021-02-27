from app import app
from flask_script import Manager,Server

manager = Manager(app)
manager.add_command('server',Server)

manager.add_command('server', Server)
@manager.command
def test():
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)

if __name__ == '__main__':
    app.run(debug=True)