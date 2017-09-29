from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import mongo
from ..models import User
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.objects.get(username=form.username.data)
        except User.DoesNotExist:
            user = None
        # if user is not None and user.verify_password(form.password.data):
        # if user is not None:
        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            # user.save()
            user.save()
            return redirect(request.args.get('next') or url_for('main.index'))
            # return redirect(url_for('main.index'))

        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        user = User()
        user.username=form.username.data
        user.password=form.password.data
        user.email=form.email.data
        user.save()

        flash('you can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
