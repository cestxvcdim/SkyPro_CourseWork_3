from flask import Blueprint, render_template, request
from utils import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__)


@search_blueprint.route('/search')
def search_page():
    search_query = request.args.get('s')
    posts = search_for_posts(search_query)
    length_posts = len(posts)
    return render_template('search.html', posts=posts, length_posts=length_posts)
