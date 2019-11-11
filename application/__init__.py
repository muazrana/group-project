from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '7589g2658d55g256582365852r2h65fg'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes