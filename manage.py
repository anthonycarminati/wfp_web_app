import os
from app import create_app
from app import db
from flask.ext.script import Manager, Server
from app.models import User


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@manager.command
def adduser(first_name, last_name, email, username, admin=False):
    """Register a new user."""
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt='Confirm: ')
    if password != password2:
        import sys
        sys.exit('Error: passwords do not match.')
    db.create_all()
    user = User(name=first_name+" "+last_name, email=email, username=username, password=password, is_admin=admin)
    db.session.add(user)
    db.session.commit()
    print('User {0} was registered successfully.'.format(username))

if __name__ == '__main__':
    # server = Server(host='0.0.0.0', port='8080')
    # manager.run(server)
    manager.run()
