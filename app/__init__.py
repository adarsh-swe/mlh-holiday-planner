import os
import re
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import (
    Flask, render_template, request, session, flash, redirect, url_for, logging
)
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import json 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}".format(
    user=os.getenv("POSTGRES_USER"),
    passwd=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=5432,
    table=os.getenv("POSTGRES_DB")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Session set up 
app.secret_key=os.getenv('SESSION_SECRET')
app.config['SESSION_TYPE'] = 'SESSION_SQLALCHEMY'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_FILE_THRESHOLD'] = 200
app.config.from_object(__name__)

class UserModel(db.Model):
    __tablename__="users"

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

# Decorator
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized access, please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=("GET", "POST"))
def register(): 
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username: 
            error = "Username is required."
        elif not password: 
            error = "Password is required."
        elif UserModel.query.filter_by(username=username).first() is not None: 
            error = f"User {username} is already registered."
        
        if error is None: 
            new_user = UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash(f'User {username} created successfully', 'success')
            return redirect(url_for('index'))
        else: 
            return error, 418

    return render_template("register.html")

@app.route('/login', methods=("GET", "POST"))
def login(): 
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None
        user = UserModel.query.filter_by(username=username).first()

        if user is None: 
            error = "Incorrect username"
            return render_template('login.html', error = error)
        elif not check_password_hash(user.password, password): 
            error = "Incorrect password."
            return render_template('login.html', error = error)
        
        if error is None: 
            session['logged_in'] = True
            session['username'] = username

            flash('You are now logged in')
            return redirect(url_for('journal'))
        else: 
            return error, 418
    return render_template("login.html")

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('Your are now logged out', 'success')
    return redirect(url_for('login'))

@app.route('/journal')
@is_logged_in
def journal():
    return render_template("journal.html")

@app.route('/flights')
def flights():
    return render_template("landing.html", filledData=False, data=None)

@app.route('/flightsAPI', methods=("GET", "POST"))
def flightsAPI(): 
    if request.method=="POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        departDate = request.form.get("departDate")
        returnDate = request.form.get("returnDate")
        error = None
    
    url = f'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/{origin}-sky/{destination}-sky/{departDate}'
    querystring = {"inboundpartialdate":returnDate}
    headers = {
        'x-rapidapi-key': os.getenv("SKYSCANNER_KEY"),
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    
    # print(response.text)
    # res = response.json()
    res = response.json()
    # return str(res)

    destination = {}
    origin = {}
    flights = [] 

    for x in res["Places"]: 
        if(x["PlaceId"] == res["Routes"][0]["DestinationId"]):
            destination = x
        elif ((x["PlaceId"] == res["Routes"][0]["OriginId"])):
            origin = x

    for x in res["Quotes"]:
        OutboundCarrier = "" 
        InBoundCarrier = "" 

        for i in res["Carriers"] :
            if (i["CarrierId"] == x["OutboundLeg"]["CarrierIds"][0]):
                OutBoundCarrier = i["Name"]

        flight = {
            "Direct" : x["Direct"],
            "Price" : x["MinPrice"],
            "Date" : x["OutboundLeg"]["DepartureDate"],
            "OutboundCarrier" : OutBoundCarrier,
            "InboundCarrier": InBoundCarrier,
        }
        flights.append(flight)


    data = { 
        "destination" : destination, 
        "origin" : origin,
        "flights" : flights
    }
    return render_template("landing.html", filledData=True, data=data)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/listing')
def listing():
    return render_template("listing.html")