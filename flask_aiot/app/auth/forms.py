from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from flask_login import current_user
from flask_mongoengine.wtf import model_form
from ..models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    # email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('keep me login in')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 128), Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64),
                                                   Regexp('^[A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, numbers dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Password mush match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.objects.filter(email=field.data).count() > 0:
            raise ValidationError('Email already registered.')

    def validata_username(self, field):
        if User.objects.filter(username=field.data).count() > 0:
            raise ValidationError('Username already in use.')
