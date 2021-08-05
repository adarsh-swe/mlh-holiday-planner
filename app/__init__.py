import os
from flask import (
    Flask, render_template, request,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all


db = SQLAlchemy()
patch_all()


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}".format(
        user=os.getenv("POSTGRES_USER"),
        passwd=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=5432,
        table=os.getenv("POSTGRES_DB"),
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create database tables for our data models
        return app