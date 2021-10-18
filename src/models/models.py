from src import db, ma
from datetime import datetime
from flask_marshmallow.fields import fields

class Post(db.Model):
	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), nullable=False)
	body = db.Column(db.String(300), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
	updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

	def __init__(self, title, body):
		self.title = title
		self.body = body

	def __repr__(self):
		return '<PostModel {}:{}>'.format(self.title, self.body)

class PostSchema(ma.Schema):
	class Meta:
		fields = ("id", "title", "body", "created_at", "updated_at")

	created_at = fields.DateTime('%Y-%m-%d %H:%M:%S')
	updated_at = fields.DateTime('%Y-%m-%d %H:%M:%S')

post_schema = PostSchema()
posts_schema = PostSchema(many=True)
