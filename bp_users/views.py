from flask import Blueprint, render_template
from utils import get_posts_by_user

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users/<username>')
def users_page(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)
