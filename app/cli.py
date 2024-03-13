import click
from flask.cli import with_appcontext
from app.models import User, ProductionRecord, ReceptionRecord
from app.extensions import db

@click.command(name="create_db")
@with_appcontext
def create_db():
    db.create_all()
    db.session.commit()
    print("Database tables created")


@click.command(name="create_admin")
@with_appcontext
def create_admin():
    if not User.query.filter_by(username='admin').first():
        new_admin = User(
            email='admin@email.com',
            username='admin',
            is_admin=True
        )
        new_admin.set_password('admin12345')
        db.session.add(new_admin)
        db.session.commit()
        print("admin created")
    else:
        print('admin already exists')


@click.command(name="create_user")
@click.option('--username', prompt='Enter user username', help='User username')
@click.option('--email', prompt='Enter user email', help='User email',required=False, default=None)
@click.option('--password', prompt='Enter user password', hide_input=True, confirmation_prompt=True, help='User password')
@with_appcontext
def create_user(username, email, password):
    if User.query.filter_by(username=username).first():
        print(f"User with username '{username}' already exists.")
        return
    
    if email and User.query.filter_by(email=email).first():
        print(f"User with username '{email}' already exists.")
        return
    
    new_user = User(
        username=username,
        is_admin=False
    )
    if email:
        new_user.email = email
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    print("User created successfully.")


@click.command(name="delete_db")
@with_appcontext
def drop_table():
    db.drop_all()
    print('database dropped')

