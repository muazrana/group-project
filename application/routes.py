from app import app, db
from flask import Flask, render_template, url_for, redirect 
from app.forms import NameForm 
from app.models import User
import boto3
import json
import random
from random import randint 
import string 

awsFunction = boto3.client('lambda', region_name='eu-west-1')


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET','POST'])
def home():
	form = NameForm()
    username = awsFunction.invoke(FunctionName='shuffle', InvocationType='RequestResponse')
    account_id = json.loads(username['Payload'].read().decode("utf-8"))

    userPrize = awsFunction.invoke(FunctionName='prize_gen',InvocationType='RequestResponse')
    prize_won = json.loads(userPrize['Payload'].read().decode("utf-8"))
    if form.validate_on_submit():
	    Users = User(name = form.name.data, 
			  account_id = account_id,
			  prize_won = prize_won) 
	    db.session.add(Users)
	    db.session.commit()
	    id = User.query.filter_by(account_id=account_id).first()
	    return redirect(url_for('result', id=id.id)
	return render_template('home.html', title='Home', form=form)
	

@app.route("/result/<int(min=1):id>")
def result(id):
	new_user = User.query.filter_by(id=id).first()
	return render_template('result.html', title='Result', new_user=new_user)
