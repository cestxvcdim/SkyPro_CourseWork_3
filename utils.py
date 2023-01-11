import json
import os


def get_posts_all() -> list[dict[str | str, int]]:
    with open(os.path.join('data', 'posts.json'), 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_all() -> list[dict[str | str, int]]:
    with open(os.path.join('data', 'comments.json'), 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name: str) -> list[dict[str | str, int]]:
    data: list[dict[str | str, int]] = get_posts_all()
    posts: list = []
    users: list = []
    for post in data:
        if post["poster_name"] == user_name.lower():
            posts.append(post)
            users.append(post["poster_name"])
    if user_name.lower() not in users:
        raise ValueError
    return posts


def get_post_by_pk(pk: int) -> dict[str | str, int] | str:
    data: list[dict[str | str, int]] = get_posts_all()
    for post in data:
        if post["pk"] == pk:
            return post
    return f'Не найдено поста с pk {pk}'


def get_comments_by_post_id(post_id: int) -> list[dict[str | str, int]]:
    data: list[dict[str | str, int]] = get_comments_all()
    comments: list = []
    posts: set = set()
    for post in data:
        if post["post_id"] == post_id:
            comments.append(post)
            posts.add(post_id)
    if post_id not in posts:
        raise ValueError
    return comments


def search_for_posts(query: str):
    data: list[dict] = get_posts_all()
    posts: list = []
    for post in data:
        if query.lower() in post["content"].lower():
            posts.append(post)
    if len(posts) == 0:
        return f'Не найдено постов по слову {query}'
    return posts
