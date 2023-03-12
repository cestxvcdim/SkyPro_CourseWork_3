from flask import Blueprint, render_template
from utils import get_posts_by_user

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/users/<username>')
def users_page(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)
