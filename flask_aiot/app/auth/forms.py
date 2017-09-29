from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,HiddenField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from flask_login import current_user
from flask_mongoengine.wtf import model_form
from ..models import User


class LoginForm(FlaskForm):
    # username = HiddenField('Username', validators=[Required(), Length(1, 64)])
    email = StringField('邮件', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('邮件', validators=[Required(), Length(1, 128), Email()])
    username = StringField('用户名', validators=[Required(), Length(1, 64),
                                                   Regexp('^[A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, numbers dots or underscores')])
    password = PasswordField('密码', validators=[Required(), EqualTo('password2', message='Password mush match.')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.objects.filter(email=field.data).count() > 0:
            raise ValidationError('Email already registered.')

    def validata_username(self, field):
        if User.objects.filter(username=field.data).count() > 0:
            raise ValidationError('Username already in use.')
