from flask import Blueprint,request,render_template
from flask.views import MethodView
from ..models import Movies
from . import main
from datetime import datetime

# defines a simple mold for working with movies,any application that deals with movies
# should provide access to its genre,its rating etc.

# movies = Blueprint('movies',__name__,template_folder='templates')

@main.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/showall/',methods=['GET'])
def ShowAllView():
    movies = Movies.objects.all()
    return render_template('list.html',movies=movies)

