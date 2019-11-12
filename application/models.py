from application import db
from datetime import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name =  db.Column(db.String(40), nullable=False)
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	account_id = db.Column(db.String(15), nullable=False, unique=True)
	prize_won = db.Column(db.String(15), nullable=False)
	

