from flask import Blueprint

api = Blueprint('posts', __name__)

@api.route('/', methods=['GET'])
def index():
	return 'Hello, BluePrint'
