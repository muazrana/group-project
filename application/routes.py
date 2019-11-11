from flask import Flask, render_template, url_for, redirect, request
from application import app, db, bcrypt
from application.models import Users
from application.forms import NameForm
from application.generator import random_with_N_digits, random_char

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
	form = NameForm()
	user = Users(name=form.name.data, account_id=account_id, prize=_prize_won)
	random_number = str(random_with_N_digits(2))
	random_letter = str(random_char(5))
	account_id = random_number + random_letter 
	db.session.add(user)
	db.session.commit()
	return render_template('home.html', title='Home', form=form)

