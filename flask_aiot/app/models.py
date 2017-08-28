from . import mongo

class Chinacwa(mongo.Document):
    article_title=mongo.StringField(required=True)
    article_title=mongo.StringField(required=True)
    article_title=mongo.StringField(required=True)
    article_title=mongo.StringField(required=True)

class Movies(mongo.Document):
    movie_id = mongo.StringField(required=True)
    rating = mongo.FloatField(required=True)
    rating_cnt = mongo.IntField(required=True)
    released = mongo.StringField(required=True)
    name = mongo.StringField(required=True)
    inserted = mongo.DateTimeField(required=True)
    img_src = mongo.StringField(required=True)
    genre = mongo.ListField(mongo.StringField(), required=True)
    description = mongo.StringField(required=True)
    duration = mongo.IntField(required=True)
    writer = mongo.ListField(mongo.StringField(), required=True)
    produced = mongo.DateTimeField(required=True)
    cast = mongo.ListField(mongo.StringField(), required=True)
    director = mongo.ListField(mongo.StringField(), required=True)

    # definition of default ordering and desired indexes
    meta = {
        'ordering': ['-rating'],
        'indexes': ['genre', 'produced', '-rating']
    }

    # meta = {'collection': 'zhenaidatabase'}
