from flask import Blueprint, render_template, flash, \
                redirect, url_for, request
from app.auth.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin_bp.usermanager'))
        return redirect(url_for('inprocess_bp.inprocess'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth_bp.login'))
        login_user(user)
        next_page = url_for('inprocess_bp.inprocess')
        if current_user.is_admin:
            next_page = url_for('admin_bp.usermanager')
        flash("You are now signed in!", "success")
        return redirect(next_page)
    return render_template('index.html', title='Login', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have signed out!", "success")
    return redirect(url_for('auth_bp.login'))
