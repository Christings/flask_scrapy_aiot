from flask import Blueprint,request,render_template
from flask.views import MethodView
from ..models import Movies
from ..models import Chinacwa
from ..models import Iot
from ..models import Ny135

from . import main
from datetime import datetime

# defines a simple mold for working with movies,any application that deals with movies
# should provide access to its genre,its rating etc.

# movies = Blueprint('movies',__name__,template_folder='templates')

@main.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/show_chinacwa/',methods=['GET'])
def ShowChinacwaView():
    chinacwa = Chinacwa.objects.all()
    return render_template('list.html',articles=chinacwa)

@main.route('/show_iot/',methods=['GET'])
def ShowIotcwaView():
    iot = Iot.objects.all()
    return render_template('list.html',articles=iot)

@main.route('/show_ny135/',methods=['GET'])
def ShowNy135cwaView():
    ny135 = Ny135.objects.all()
    return render_template('list.html',articles=ny135)