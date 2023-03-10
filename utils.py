import json
import os


def get_posts_all() -> list[dict[str, str | int]]:
    with open(os.path.join('data', 'posts.json'), 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_all() -> list[dict[str, str | int]]:
    with open(os.path.join('data', 'comments.json'), 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name: str) -> list[dict[str, str | int]]:
    data: list[dict[str, str | int]] = get_posts_all()
    posts: list = []
    for post in data:
        if post["poster_name"] == user_name.lower():
            posts.append(post)
    return posts


def get_post_by_pk(pk: int) -> dict[str, str | int] | dict:
    data: list[dict[str, str | int]] = get_posts_all()
    for post in data:
        if post["pk"] == pk:
            return post
    return {}


def get_comments_by_post_id(post_id: int) -> list[dict[str, str | int]]:
    data: list[dict[str, str | int]] = get_comments_all()
    comments: list = []
    posts: set = set()
    for post in data:
        if post["post_id"] == post_id:
            comments.append(post)
            posts.add(post_id)
    if post_id not in posts:
        raise ValueError("Такого поста нет")
    return comments


def search_for_posts(query: str) -> list[dict[str, str | int]] | str:
    data: list[dict[str, str | int]] = get_posts_all()
    posts: list = []
    for post in data:
        if query.lower() in post["content"].lower():
            posts.append(post)
    return posts


def count_comments(comments_count: int) -> str:
    reminder: int = comments_count % 10
    if 5 <= reminder <= 9 or reminder == 0:
        return f"{comments_count} комментариев"
    if reminder == 1:
        return f"{comments_count} комментарий"
    if 2 <= reminder <= 4:
        return f"{comments_count} комментария"


def search_by_tag(tag: str) -> list[dict[str, str | int]]:
    data: list[dict[str, str | int]] = get_posts_all()
    posts: list = []
    for post in data:
        if tag.lower() in post["content"]:
            posts.append(post)
    return posts
