import pytest
import httpx
import json

def test_get() -> None:
    url: str = "http://localhost:8000/home/"
    resp: httpx = httpx.get(url)
    assert resp.status_code == 200
def test_get_all_movies() -> None:
    url: str = "http://localhost:8000"
    resp = httpx.get(url)
    assert resp.status_code == 200
def test_create_movie() -> None:
    url: str = "http://localhost:8000/movie/create/"
    new_movie = {
        "title": "Back To The Future",
        "description": "Science-fiction about time travel",
        "image": "http://localhost:8000/media/movie/images/back-to-the-future_poster_Tl9pr6s.jpg"
    }
    resp = httpx.post(url=url, content=json.dumps(new_movie))
    assert resp.status_code == 201
    assert resp.text == json.dumps(new_movie)
