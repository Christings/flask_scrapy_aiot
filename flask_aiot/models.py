from flask_imdb import db


class Movies(db.Document):
    movie_id = db.StringField(required=True)
    rating = db.FloatField(required=True)
    rating_cnt = db.IntField(required=True)
    released = db.StringField(required=True)
    name = db.StringField(required=True)
    inserted = db.DateTimeField(required=True)
    img_src = db.StringField(required=True)
    genre = db.ListField(db.StringField(), required=True)
    description = db.StringField(required=True)
    duration = db.IntField(required=True)
    writer = db.ListField(db.StringField(), required=True)
    produced = db.DateTimeField(required=True)
    cast = db.ListField(db.StringField(), required=True)
    director = db.ListField(db.StringField(), required=True)

    # definition of default ordering and desired indexes
    meta = {
        'ordering': ['-rating'],
        'indexes': ['genre', 'produced', '-rating']
    }
