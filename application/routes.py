from flask import Flask, render_template, url_for, redirect, request
from application import app, db, bcrypt
from application.models import Users

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', title='Home')