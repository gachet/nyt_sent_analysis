#!flask/bin/python

import requests, json, scraper, ast
from flask import Flask, Response, render_template, redirect, url_for, request, make_response, jsonify
from app import app
from models import User, Articles
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from uri import parse_query, get_movie_reviews, get_book_reviews
import logging

logging.basicConfig()

# import CONFIG variables for OAuth
CONFIG = app.config['CONFIG']

# instantiate Authomatic
authomatic = Authomatic(CONFIG, 'password', report_errors=True)

class Result:
	r = None

result = Result()

@app.route('/')
def lanch():
	return render_template('main.html')

# login route
@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
	# make response object
	response = make_response()

	# log the user in
	result.r = authomatic.login(WerkzeugAdapter(request, response), provider_name)
	if result.r:
		if result.r.user:
			result.r.user.update()
		return redirect(url_for('home'))
	return response


@app.route('/home')
def home():
	# query for the user data if user is already in db 
	if User.query.filter_by(email=result.r.user.email).first() is None:
		print 'no user by that name'
		user = User(result.r.user.name, result.r.user.email)
		print user 
	else:
		print 'user exists'
	return render_template('home.html', result=result.r)


@app.route('/search', methods=['POST'])
def get_keywords():
	text = request.form['text']
	return redirect(url_for('search', keyword=text))


# route to render search movie results
@app.route('/results/<keyword>')
def search(keyword):
	request_uri = get_movie_reviews(keyword)
	resp = requests.get(request_uri).json()
	# get number of pages needed for all results
	if resp['num_results'] % 20 > 0 and resp['num_results'] / 20 >= 1:
		pages = (resp['num_results'] / 20) + 1
	elif resp['num_results'] % 20 == 0 and resp['num_results'] / 20 >= 1:
		pages = resp['num_results'] / 20
	elif resp['num_results'] <= 20: 
		pages = 1
	print 'Number of results: ', json.dumps(resp['num_results'], indent=2)
	# print 'Number of pages: ', pages
	return render_template('results.html', reviews=resp, pages=pages)


# scrape nytimes article and return data
@app.route('/results/<keyword>', methods=['POST'])
def scrape(keyword):
	url = json.loads(request.data)['nyt_url']
	text = scraper.article_scraper(url)
	# send text to external link to process for sentiment analysis
	response = requests.post('http://text-processing.com/api/sentiment/', data={'text': text})
	print response.text
	# return json.dumps(response.text, indent=2)
	return 'SUCCESS'

