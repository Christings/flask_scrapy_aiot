from . import mongo, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class Chinacwa(mongo.Document):
    article_id = mongo.IntField(required=True)
    article_title = mongo.StringField(required=True)
    article_keywords = mongo.StringField(required=True)
    article_url = mongo.StringField(required=True)
    article_abstract = mongo.StringField(required=True)
    article_content = mongo.StringField(required=True)

    meta = {
        'collection': 'chinacwa',
        'ordering': ['-article_id'],
        'indexes': ['-article_id']
    }


class Iot(mongo.Document):
    article_title = mongo.StringField(required=True)
    article_keywords = mongo.StringField(required=True)
    article_url = mongo.StringField(required=True)
    article_abstract = mongo.StringField(required=True)
    article_content = mongo.StringField(required=True)

    meta = {'collection': 'iot'}


class Ny135(mongo.Document):
    article_title = mongo.StringField(required=True)
    article_keywords = mongo.StringField(required=True)
    article_url = mongo.StringField(required=True)
    article_abstract = mongo.StringField(required=True)
    article_content = mongo.StringField(required=True)
    meta = {'collection': 'ny135'}


class AllProductPrice(mongo.Document):
    product_name = mongo.StringField(required=True)
    product_price = mongo.StringField(required=True)
    product_market = mongo.StringField(required=True)
    product_releasedate = mongo.StringField(required=True)
    meta = {'collection': 'allproductprice'}


class User(UserMixin, mongo.Document):
    # uid = mongo.IntField(requires=True)
    email = mongo.StringField(max_length=255, requires=True)
    username = mongo.StringField(max_length=255, requires=True)
    # password = mongo.StringField(requires=True)
    password_hash = mongo.StringField(requires=True)
    # confirmed=mongo.BooleanField(default=False)
    # password_hash = mongo.StringField(requires=True)
    # meta = {'collection': 'user'}

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.email

    def get_id(self):
        try:
            # return unicode(self.username)
            return self.email
        except AttributeError:
            raise NotImplementedError('No `username` attribute - override `get_id`')

    def __unicode__(self):
        return self.email

        # def confirm(self,token):
        #     s=Serializer(current_app.config['SECRET_KEY'])
        #     try:
        #         data=s.loads(token)
        #     except:
        #         return False
        #     if data.get('confirm')!=self.username
        #         return False
        #     self.confirmd=True


@login_manager.user_loader
def load_user(email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None
    return user

