from application import db
from datetime import datetime

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name =  db.Column(db.String(40), nullable=False)
	date_created = db.Column(db.DateTime, nullabe=False, default=datetime.utcnow)
	account = db.Column(db.String(5), nullabe=False, unique=True)
	prize_won = db.Column(db.String(15), nullabe=False)

