from flask_login import current_user
from functools import wraps
from flask import flash, redirect, url_for


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.is_admin != True:
            flash("You need to be an admin to view this page.","danger")
            return redirect(url_for('auth_bp.login'))
        return f(*args, **kwargs)

    return decorated_function