import pytest
import httpx
import json


SERVER = "http://localhost:8000"
def test_get() -> None:
    url: str = f"{SERVER}/home/"
    resp: httpx = httpx.get(url)
    assert resp.status_code == 200
def test_user_behavior() -> None:
    # USER VISITS HOMEPAGE
    url: str = f"{SERVER}/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    # USER LOGINS
    url: str = f"{SERVER}/accounts/signupaccount/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    user = "user1"
    password = "password1"
    resp = httpx.post(url=url, content=user)
    resp = httpx.post(url=url, content=password)
    resp.status_code = 302
    # USER VISITS PARTICULAR MOVIE
    url = f"{SERVER}/23c30cd3-49e8-433a-a460-0aed26f0a92a"
    resp = httpx.get(url)
    assert resp.status_code == 200
    # USER WANTS TO ADD REVIEW
    url = f"{SERVER}/23c30cd3-49e8-433a-a460-0aed26f0a92a/create"
    resp = httpx.get(url)
    assert resp.status_code == 200

def test_get_all_movies() -> None:
    url: str = f"{SERVER}/"
    resp = httpx.get(url)
    assert resp.status_code == 200
def test_get_review() -> None:
    url = f"{SERVER}/23c30cd3-49e8-433a-a460-0aed26f0a92a/create"
    resp = httpx.get(url)
    assert resp.status_code == 200
def test_create_movie() -> None:
    url: str = f"{SERVER}/movie/create/"
    new_movie = {
        "title": "Back To The Future",
        "description": "Science-fiction about time travel",
        "image": "http://localhost:8000/media/movie/images/back-to-the-future_poster_Tl9pr6s.jpg"
    }
    resp = httpx.post(url=url, content=json.dumps(new_movie))
    assert resp.status_code == 201
    assert resp.text == json.dumps(new_movie)
