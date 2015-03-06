app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/development'

from models import db
db.init_app(app)