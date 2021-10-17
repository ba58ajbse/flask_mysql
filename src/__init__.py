from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('./instance/config/development.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
