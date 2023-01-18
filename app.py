import logging
from flask import Flask, jsonify
from bp_main.views import main_blueprint
from bp_post.views import post_blueprint
from bp_search.views import search_blueprint
from bp_users.views import users_blueprint
from bp_tags.views import tag_blueprint
from utils import get_posts_all, get_post_by_pk

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(tag_blueprint)
app.static_folder = app.root_path + "/static/"

logging.basicConfig(filename='api.log', level=logging.INFO, encoding='utf-8')
logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")


@app.route('/api/posts')
def api_posts():
    logging.info("Зашел на api по всем пользователям")
    posts = get_posts_all()
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>')
def api_post(post_id):
    logging.info(f"Зашел на api по {post_id} пользователю")
    post = get_post_by_pk(post_id)
    return jsonify(post)


@app.errorhandler(404)
def not_found_404(e):
    return "<h1>Not found</h1>", 404


@app.errorhandler(500)
def not_found_500(e):
    return "<h1>Internal Server Error</h1>", 500


if __name__ == '__main__':
    app.run()
