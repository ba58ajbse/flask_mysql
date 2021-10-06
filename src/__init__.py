from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('./instance/config/development.py')

db = SQLAlchemy(app)
