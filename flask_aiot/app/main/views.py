from flask import Blueprint, request, render_template
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

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/show_chinacwa/', methods=['GET'])
def ShowChinacwaView(page=1):
    # page=request.args.get('page',1,type=int)
    pagination = Chinacwa.objects.paginate(page=page, per_page=20)
    # chinacwa=pagination.items
    chinacwa = Chinacwa.objects.all()
    return render_template('list.html', articles=chinacwa, pagination=pagination)


@main.route('/show_iot/', methods=['GET'])
def ShowIotcwaView(page=1):
    iot = Iot.objects.all()
    pagination = Iot.objects.paginate(page=page, per_page=20)
    return render_template('list.html', articles=iot,pagination=pagination)


@main.route('/show_ny135/', methods=['GET'])
def ShowNy135cwaView(page=1):
    ny135 = Ny135.objects.all()
    pagination = Ny135.objects.paginate(page=page, per_page=20)
    return render_template('list.html', articles=ny135,pagination=pagination)
