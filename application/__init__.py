
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@mysql/flaskapp'
app.config['SECRET_KEY'] = '7589g2658d55g256582365852r2h65fg'

db = SQLAlchemy(app)


from application import route






