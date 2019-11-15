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

if __name__ == '__main__':
		app.run(debug=True, host="0.0.0.0")
