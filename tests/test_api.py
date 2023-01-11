import pytest
from app import app

keys_should_be = [
    "poster_name"
    "poster_avatar"
    "pic"
    "content"
    "views_count"
    "likes_count"
    "pk"
]


class TestApi:

    def test_api_posts(self):
        response = app.test_client().get('/api/posts')
        wrong_json = []
        for post in response.json:
            for key in keys_should_be:
                if post.get(key) is None:
                    wrong_json.append(post)

        assert isinstance(response.json, list), "Wrong data"
        assert wrong_json == [], "Wrong JSON"

    def test_api_post(self):
        response = app.test_client().get("/api/posts/1")
        wrong_dicts = []
        for key in keys_should_be:
            if response.json.get(key) is None:
                wrong_dicts.append(key)

        assert isinstance(response.json, dict), "Wrong data"
        assert wrong_dicts == [], "Wrong dict(s)"
