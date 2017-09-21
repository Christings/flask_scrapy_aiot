from . import mongo


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
