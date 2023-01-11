from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts')
def api_posts():
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<post_id>')
def api_post(post_id):
    post = get_post_by_pk(post_id)
    return jsonify(post)


