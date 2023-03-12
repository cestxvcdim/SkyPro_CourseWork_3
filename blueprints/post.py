from flask import Blueprint, render_template
from utils import get_comments_by_post_id, get_post_by_pk, count_comments

post_blueprint = Blueprint('post_blueprint', __name__)


@post_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    try:
        comments = get_comments_by_post_id(post_id)
        post = get_post_by_pk(post_id)
        count_coms = count_comments(len(comments))
        return render_template('post.html', comments=comments, post=post, id=post_id, count_coms=count_coms)
    except ValueError:
        return 'Такого поста нет'