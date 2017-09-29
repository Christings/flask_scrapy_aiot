## Project Description

That is a simple Python project illustrating the use of the following:

Scrapy (scraping and crawling framework)
Flask (micro web development framework based on Werkzeug)
The project is split up into two subprojects located in the respective folders. We firstly scrape the Agricultural Database with the aim to get information for Agriculture we are interesting in. This information is persistenly stored in the mongodb database. Given that a data can be represented as a document, mongodb was considered the best match for that use case. The second subproject corresponds to a web application being responsible for rendering the data we gathered from Internet.


## Installation

If you have Virtualenv installed you can simply run Virtualenvto get a running environment.

To manually install the prerequisites on a ubuntu/debian system you can type the following in your shell.

# install mongo and python
sudo apt-get install -y mongodb python-dev python-pip python-lxml
# install python packages
sudo pip install -r requirements.txt
# create mongo index for speeding up queries
mongo scripts/create_index.js
Components

###scrapy_aiot Location: scrapy_aiot

Goal of our scraping application is to fetch information about Agricultural information. For example: name, price, market, releasedate, etc. We specify a url that corresponds to a list assembled by argiculture itself, or by a user. E.g. top-250 movies (http://www.imdb.com/chart/top). Then the scrapy spider parses this list and for every movie existing there it acquires information. This information is later being stored to imdb.movies collection of mongodb database by the implemented pipeline.

###flask_imdb Location: flask_aiot

A web application was implemented to present the aforementioned movie related information in a human friendly manner. This application is backed up by a server provided by the flask framework. Server listens for user requests and dispatces these requests to the corresponding views. A sidebar allowing for predefined queries exists. The user can also issue a request to the server by typing a movie's name (or part of it, a rating (1-10), a desired genre (e.g. crime), or a specific year.

Filling out mongodb collection

cd 待续
scrapy crawl aiot
This opetation will take some time and after its execution a number of movies will exist in the movies collection of the imdb mongodb.

Starting the flask server

Once spider and pipeline have completed, the server can be started and content can be served to the user via the web browser. In order to start the server simply type:

cd 待续
python manage.py runserver
Check web page

Open your preferred browser and type in the location bar: http://localhost:5000/index

Cleanup

Execute the following commands for dropping the movies collection:

mongo imdb --eval "db.movies.drop()"
For dropping the whole imdb database please execute:

mongo imdb --eval "db.dropDatabase()"
  