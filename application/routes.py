#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, url_for, redirect, request
from application import app, db
from application.models import User
from application.forms import NameForm
import random

from  flask import Flask, render_template, url_for, redirect 
from application.form import NameForm 
import boto3
import json
import random
import string 

app= Flask(__name__)
awsFunction = boto3.client('lambda', eu-west-1'

@app.route("/")
@app.route("/home")
def home():
	username = awsFunction.invoke(
				   FunctionName='shuffle',
				   InvocationType='RequestResponse'
				   )
	account_id = json.loads(username['Payload'].read().decode("utf-8"))

	userPrize = awsFunction.invoke(
				    FunctionName='prize_gen',
				    InvicationType='RequestResponse'
	prize = json.loads(userPrize['Payload'].read().decode("utf-8"))
	package = send_data(
			    )



@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET','POST'])
def home():
	  form = NameForm()
	  prize_list = ['House', '£10,000', '£100,000', 'Car', 'Mac Computer', 'Ipad', 'Iphone 11 pro', 'Package holiday', '£10','£20', '£50']
	  prize_won=(random.choice(prize_list))
	  random_number = str(random_with_N_digits(2))
	  random_letter = str(random_char(5))
	  account_id = random_number + random_letter
	  if form.validate_on_submit(): 
	  	user = User(name=form.name.data, account_id=account_id, prize_won=prize_won)
	  	db.session.add(user)
	  	db.session.commit()
	  	id = User.query.filter_by(account_id=account_id).first()
	  	return redirect(url_for('result', id=id.id))
	  return render_template('home.html', title='Home', form=form)

@app.route("/result/<int(min=1):id>")
def result(id):
	new_user = User.query.filter_by(id=id).first()
	return render_template('result.html', title='Result', new_user=new_user)
