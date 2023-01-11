import logging
from flask import Flask
from bp_main.views import main_blueprint
from bp_post.views import post_blueprint
from bp_search.views import search_blueprint
from bp_users.views import users_blueprint
from api.views import api_blueprint
from bp_tags.views import tag_blueprint

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(tag_blueprint)
app.static_folder = app.root_path + "/static/"

logging.basicConfig(filename='api.log', level=logging.INFO, encoding='utf-8')
logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")


@app.errorhandler(404)
def not_found_404(e):
    return "<h1>Not found</h1>", 404


@app.errorhandler(500)
def not_found_500(e):
    return "<h1>Internal Server Error</h1>", 500


app.run()
