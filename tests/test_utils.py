import pytest
from utils import *


class TestUtils:

    def test_get_posts_by_user(self):
        posts = get_posts_by_user('leo')
        assert isinstance(posts, list), 'возвращается не список'
        assert len(posts) > 1, 'возвращается пустой список'
        with pytest.raises(ValueError):
            get_posts_by_user('*$@#')

    def test_get_post_by_pk(self):
        assert {} == get_post_by_pk(0)
        post = get_post_by_pk(4)
        assert post.get("poster_name") == 'larry'
        assert post.get("likes_count") == 198

    def test_get_comments_by_post_id(self):
        comments = get_comments_by_post_id(1)
        assert isinstance(comments, list), 'возвращается не список'
        with pytest.raises(ValueError):
            get_comments_by_post_id(0)

    def test_search_for_posts(self):
        posts = search_for_posts('закат')
        assert isinstance(posts, list), 'возвращается не список'
        assert len(posts) >= 1, 'ошибка в функции'

    def test_count_comments(self):
        assert "1 комментарий" == count_comments(1)
        assert "4 комментария" == count_comments(4)
        assert "5 комментариев" == count_comments(5)
        assert "9 комментариев" == count_comments(9)
        assert "0 комментариев" == count_comments(0)
        assert "126 комментариев" == count_comments(126)
