#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, url_for, redirect, request
from application import app, db
from application.models import User
from application.forms import NameForm
from application.generator import random_with_N_digits, random_char
import random
prize_list = ['House', '£10,000', '£100,000', 'Car', 'Mac Computer', 'IPAD', 'Iphone 11 pro', 'Package holiday' ]
prize_won=(random.choice(prize_list))



@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
	  form = NameForm()
	  random_number = str(random_with_N_digits(2))
	  random_letter = str(random_char(5))
	  account_id = random_number + random_letter 
	  user = User(name=form.name.data, account_id=account_id, prize_won=prize_won)
	  db.session.add(user)
	  db.session.commit()
	  return redirect(url_for('result'))
	  return render_template('home.html', title='Home', form=form)

@app.route("/result", methods=['GET', 'POST'])
def result():
	User = User.query.all()
	return render_template('result.html', title='Result', user=user)