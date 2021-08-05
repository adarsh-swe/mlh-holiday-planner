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

from flask import (
    Flask, render_template, request,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")