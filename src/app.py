from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
dbname = os.getenv('DB_NAME')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{dbname}'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        post = Post(title=title, body=body)

        db.session.add(post)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create.html')

@app.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    else:
        post.title = request.form.get('title')
        post.body = request.form.get('body')

        db.session.commit()
        return redirect('/')

@app.route('/<int:id>/delete', methods=['GET'])
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')
