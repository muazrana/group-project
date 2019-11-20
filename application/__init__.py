
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import config 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri.config
app.config['SECRET_KEY'] =  secret_key.config

db = SQLAlchemy(app)


from application import routes






