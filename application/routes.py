#!/usr/bin/python
# -*- coding: UTF-8 -*-

from  flask import Flask, render_template, url_for, redirect 
from app import app, db
from flask import Flask render_template, url_for, redirect 
from application.form import NameForm 
from application.models import Users
import boto3
import json
import boto3
import random
from random import randint 
import string 

awsFunction = boto3.client('lambda', region_name='eu-west-1')

app= Flask(__name__)
awsFunction = boto3.client('lambda', eu-west-1'

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET','POST'])
def home():
     form = NameForm()
     username = awsFunction.invoke(
				   FunctionName='shuffle',
				   InvocationType='RequestResponse'
				   )
     account_id = json.loads(username['Payload'].read().decode("utf-8"))

     userPrize = awsFunction.invoke(
				    FunctionName='prize_gen',
				    InvicationType='RequestResponse'
     prize_won = json.loads(userPrize['Payload'].read().decode("utf-8"))
     if form.validate_on_submit():
	     User = Users( name = form.name.data, 
			  account_id = account_id,
			  prize_won = prize_won) 
	     db.session.add(User)
	     db.session.commit()
	     id = User.query.filter_by(account_id=account_id).first()
	     return redirect(url_for('result', id=id.id)
	return render_template('home.html', title='Home', form=form)
	

@app.route("/result/<int(min=1):id>")
def result(id):
	new_user = User.query.filter_by(id=id).first()
	return render_template('result.html', title='Result', new_user=new_user)
