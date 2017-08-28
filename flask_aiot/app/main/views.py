from flask import Blueprint,request,render_template
from flask.views import MethodView
from ..models import Movies
from . import main
from datetime import datetime

# defines a simple mold for working with movies,any application that deals with movies
# should provide access to its genre,its rating etc.

# movies = Blueprint('movies',__name__,template_folder='templates')

class Index(MethodView):
	"""Index page of the application"""
	def get(self):
		return render_template('index.html')

class ShowAllView(MethodView):
	"""Retrieves and returns all the movies in the mongodb collection"""
	def get(self):
		movies = Movies.objects.all()
		return render_template('list.html',movies=movies)

class RatingView(MethodView):
	"""Returns the movies having a specific rating:"""
	def get(self,rating=None):
		if rating is None:
			movies = Movies.objects.all()
		else:
			movies = Movies.objects(rating=rating)
		return render_template('list.html',movies=movies)					

class NameLikeView(MethodView):
	"""Searches in an SQL like manner for movies containing a specific pattern"""
	def get(self,name_like = None):
		movies = Movies.objects(name__icontains = name_like)
		return render_template('list.html',movies = movies)

class GenreView(MethodView):
	"""Class responsible for retrieving all movies belonging to a specified genre"""
	def get(self,genre = None):
		if genre is None:
			movies = Movies.objects.all()
		else:
			movies = Movies.objects(genre__iexact=genre)
		return render_template('list.html',movies = movies)	

class ProducedView(MethodView):
	""" Renders movies being produced in a specific year."""
	def get(self,year):
		movies = Movies.objects(produced=datetime.strptime(year,"%Y"))
		return render_template('list.html',movies=movies)		

class RecentView(MethodView):
	"""Results in a bunch of movies that were produced recently"""
	def get(self):
		target_year = datetime.now().year - 10
		movies = Movies.objects(produced__gte=datetime.strptime(str(target_year),"%Y"))
		return render_template('list.html',movies=movies)

class DontWatchView(MethodView):
    """
    Finds movies whose rating is below a threshold. I.e. 6/10.
    """
    def get(self):
        movies = Movies.objects(rating__lt=8.2)
        return render_template('list.html', movies=movies)


class TopView(MethodView):
    """
    This class retrieves the top-k movies existing in the database. K is
    is passed as a parameter. The actual number of existing movies is
    found and based on that and the value of K we figure out which movies
    should be displayed.
    """
    def get(self, percentage):
        cnt = Movies.objects().count()
        limit = cnt * int(percentage) / float(100)
        movies = Movies.objects[:int(round(limit, 0))]
        return render_template('list.html', movies=movies)


class SearchView(MethodView):
    """
    This class implements the logic behind the search form. A value that
    could be either numerix or text is passed to the post function. We
    firsly treat this value as a number. In case a ValueError is raised
    (value is not numeric) we continue our searching on text fields. The
    order we follow is: genre, duration, produced, name.
    """
    def post(self):
        text = request.form['text']

        # numbers first - easier to ask forgiveness than permission
        movies = []
        try:
            movies = Movies.objects(produced=datetime.strptime(text, "%Y"))

        except ValueError:
            # still numbers
            try:
                movies = Movies.objects(rating=float(text))

                # if we found nothing we intentionally raise an error
                # and we jump to the non-numeric checks
                if not movies:
                    raise ValueError

            # text is not numeric
            except ValueError:

                # search by movie name
                movies = Movies.objects(name__icontains=text)

                if not movies:
                    # text is genre
                    movies = Movies.objects(genre__iexact=text)

        return render_template('list.html', movies=movies)


# Register the urls
main.add_url_rule('/index', view_func=Index.as_view('index_view'))
main.add_url_rule('/', view_func=Index.as_view('index_view2'))

main.add_url_rule('/rating/<float:rating>/', view_func=RatingView.as_view('rating'))
main.add_url_rule('/rating', view_func=RatingView.as_view('all_rating'))
main.add_url_rule('/rating/', view_func=RatingView.as_view('all_rating2'))

main.add_url_rule('/name/<name_like>/', view_func=NameLikeView.as_view('name_like'))

main.add_url_rule('/genre/<genre>/', view_func=GenreView.as_view('genre'))
main.add_url_rule('/genre', view_func=GenreView.as_view('all_genre'))
main.add_url_rule('/genre/', view_func=GenreView.as_view('all_genre2'))

main.add_url_rule('/produced/<year>', view_func=ProducedView.as_view('produced_in'))

main.add_url_rule('/search', view_func=SearchView.as_view('search_view'))

main.add_url_rule('/top/<percentage>', view_func=TopView.as_view('top_view'))

main.add_url_rule('/recent/', view_func=RecentView.as_view('recent_view'))

main.add_url_rule('/dontwatch/', view_func=DontWatchView.as_view('dont_watch_view'))

main.add_url_rule('/showall/', view_func=ShowAllView.as_view('show_all_view'))





