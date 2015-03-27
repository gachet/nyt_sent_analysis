from app import db

# stores users
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(120), unique=True)
	authenticated = db.Column(db.Boolean, default=False)

	def is_active(self):
		return True

	def get_email(self):
		return self.email

	def is_authenticated(self):
		return self.authenticated
	
	def __repr__(self):
		return '<User %r>' % (self.name)

# stores articles starred by users
class Articles(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Article %r>' % (self.title)