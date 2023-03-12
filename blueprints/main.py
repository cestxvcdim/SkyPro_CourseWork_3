from flask import Blueprint, render_template
from utils import get_posts_all

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)
