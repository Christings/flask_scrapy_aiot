from flask import Blueprint, request, render_template
from flask.views import MethodView
from ..models import Movies
from ..models import Chinacwa
from ..models import Iot
from ..models import Ny135
from ..models import AllProductPrice

from . import main
from datetime import datetime


# defines a simple mold for working with movies,any application that deals with movies
# should provide access to its genre,its rating etc.

# movies = Blueprint('movies',__name__,template_folder='templates')

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/show_chinacwa/', methods=['GET'])
def ShowChinacwaView():
    cnt = Chinacwa.objects.count()
    # limit=cnt*int(10)/

    page = request.args.get('page', 1, type=int)
    pagination = Chinacwa.objects.paginate(page=page, per_page=10, error_out=False)
    chinacwa = pagination.items
    # chinacwa = Chinacwa.objects.all()
    return render_template('list.html', articles=chinacwa, pagination_chinacwa=pagination)


@main.route('/show_iot/', methods=['GET'])
def ShowIotView(page=1):
    page = request.args.get('page', 1, type=int)
    pagination = Iot.objects.paginate(page=page, per_page=20)
    iot = pagination.items
    return render_template('list.html', articles=iot, pagination_iot=pagination)


@main.route('/show_ny135/', methods=['GET'])
def ShowNy135View(page=1):
    page = request.args.get('page', 1, type=int)
    pagination = Ny135.objects.paginate(page=page, per_page=20)
    ny135 = pagination.items
    return render_template('list.html', articles=ny135, pagination_ny135=pagination)


@main.route('/show_allproductprice/', methods=['GET'])
def ShowAllProductPriceView():
    page = request.args.get('page', 1, type=int)
    pagination = AllProductPrice.objects.paginate(page=page, per_page=20)
    allproductprice = pagination.items
    return render_template('PriceDataList.html', products=allproductprice, pagination_allproductprice=pagination)


@main.route('/search', methods=['POST'])
def SearchView():
    text = request.form['text']

    articles = []
    try:
        articles = Chinacwa.objects(article_id=int(text))

    except ValueError:
        # still numbers
        try:
            articles = Chinacwa.objects(article_abstract__icontains=text)

            # if we found nothing we intentionally raise an error
            # and we jump to the non-numeric checks
            if not articles:
                raise ValueError

        # text is not numeric
        except ValueError:

            # search by movie name
            articles = Chinacwa.objects(article_title__icontains=text)

            if not articles:
                # text is genre
                articles = Chinacwa.objects(article_keywords__icontains=text)

    return render_template('list.html', articles=articles)
