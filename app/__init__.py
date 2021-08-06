<<<<<<< HEAD
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
=======
# <<<<<<< HEAD
# from flask import Flask
# =======
# from flask import (
#     Flask, render_template, request,
# )
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# >>>>>>> f0833b60b4a1562de186012a1481858b26e07501

# app = Flask(__name__)


# @app.route('/')
# <<<<<<< HEAD
# def hello():
#     return 'Hello, World!'
# =======
# def index():
#     return render_template("index.html")
# >>>>>>> f0833b60b4a1562de186012a1481858b26e07501

>>>>>>> 7657eb209eac350cd0d01ab6365ae61f31edc29a
from flask import (
    Flask, render_template, request,
)
from werkzeug.security import generate_password_hash, check_password_hash

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
print(os.getenv("POSTGRES_USER"))

class UserModel(db.Model):
    __tablename__="users"

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

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
            return f"User {username} created successfully"
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
        elif not check_password_hash(user.password, password): 
            error = "Incorrect password."
        
        if error is None: 
            return "Login Successful", 200
        else: 
            return error, 418

    return render_template("login.html")