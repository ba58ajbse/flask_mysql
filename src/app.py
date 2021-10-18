from flask import request, jsonify, abort
from . import app, db
from .models.models import Post, posts_schema, post_schema
from datetime import datetime
from src.api.posts import api

app.register_blueprint(api)

@app.route('/posts/', methods=['GET'])
def get_all():
	posts = Post.query.all()

	return jsonify({'posts': posts_schema.dump(posts)})

@app.route('/posts/', methods=['POST'])
def create():
	data = request.json
	title = data.get('title')
	body = data.get('body')

	post = Post(title=title, body=body)

	db.session.add(post)
	db.session.commit()

	return jsonify({'title': title, 'body': body})

@app.route('/posts/<int:id>/', methods=["GET"])
def get(id):
	post = Post.query.filter_by(id=id).first()

	return jsonify({'post': post_schema.dump(post)})

@app.route('/posts/<int:id>/', methods=["DELETE"])
def delete(id):
	post = Post.query.filter_by(id=id).first()

	if not post:
		abort(404, {'code': 'Not found', 'message': 'post not found'})

	db.session.delete(post)
	db.session.commit()

	return jsonify(None), 204

@app.route('/posts/<int:id>/', methods=['PUT'])
def update(id):
	post = Post.query.filter_by(id=id).first()

	if not post:
		return jsonify({'code': 'Not found', 'message': 'post not found'}), 404

	data = request.json
	post.title = data.get('title')
	post.body = data.get('body')
	post.updated_at = datetime.now()

	db.session.commit()
	return jsonify({'post': post_schema.dump(post)})

if __name__ == '__main__':
	app.run()
