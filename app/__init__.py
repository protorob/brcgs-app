from flask import Flask
from app.cli import create_admin,create_db,drop_table,create_user
from app.config import Config
from app.models import User
from app.extensions import db,login_manager,bcrypt
from flask_migrate import Migrate


def create_app(config_class = Config):
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    Migrate(app)
    bcrypt.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'
    login_manager.login_message = "Please Login First"
    login_manager.login_message_category = "danger"
    
    
    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(int(user_id))

    app.cli.add_command(create_db)
    app.cli.add_command(create_admin)
    app.cli.add_command(drop_table)
    app.cli.add_command(create_user)
    
    
    from app.admin.routes import admin_bp
    app.register_blueprint(admin_bp, url_prefix="/")
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/")
    from app.reception.routes import reception_bp
    app.register_blueprint(reception_bp, url_prefix="/")
    from app.inprocess.routes import inprocess_bp
    app.register_blueprint(inprocess_bp, url_prefix="/")
    from app.fulfillment.routes import fulfillment_bp
    app.register_blueprint(fulfillment_bp, url_prefix="/")
    
    return app