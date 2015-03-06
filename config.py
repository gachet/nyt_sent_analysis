from authomatic.providers import oauth2

CONFIG = {
	'google': {
		'class_': oauth2.Google,
		'consumer_key': '88709490925-p5qr3lere7p4jlt34v2qco4vjjo4ca4c.apps.googleusercontent.com',
		'consumer_secret': 'OGxNf2sYVG4hSXgBjpbIGAhX',
		'scope': ['profile', 'email'],
	}
}

MOVIE_REVIEWS = '8f6e020d10d7a00de2195cd4cdba39b3:16:70705826'
BOOK_REVIEWS = '3055744dea8ca3ae5439d5502c0563d4:2:70705826'