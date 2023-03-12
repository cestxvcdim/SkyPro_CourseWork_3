from flask import Blueprint, render_template
from utils import search_by_tag

tag_blueprint = Blueprint('tag_blueprint', __name__)


@tag_blueprint.route('/tag/<tag_name>')
def tag_page(tag_name):
    posts = search_by_tag('#' + tag_name)
    if posts:
        count_posts = len(posts)
        return render_template('tag.html', posts=posts, count_posts=count_posts, tag_name=tag_name)
    return 'По вашему запросу ничего не найдено'
