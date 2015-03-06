from config import BOOK_REVIEWS, MOVIE_REVIEWS
from datetime import date, timedelta

def parse_query(query):
	query = query.split(' ')
	for x in range(len(query)-1):
		query[x] += '+'
	return ''.join(query)


def get_movie_reviews(query):
	if ' ' in query:
		query = parse_query(query)

	# end_date = date.today().strftime("%Y%m%d") 
	# begin_date = date.today() - timedelta(days=(5*365))
	# begin_date = begin_date.strftime("%Y%m%d")

	base_url = 'http://api.nytimes.com/svc/movies/v2/reviews/search.json?query='
	base_url += (query + '&api-key=' + MOVIE_REVIEWS)

	return base_url

def get_book_reviews(query):
	if ' ' in query:
		query = parse_query(query)

	base_url = 'http://api.nytimes.com/svc/books/v3/reviews.json?title='
	base_url += (query + '&api-key=' + BOOK_REVIEWS)

