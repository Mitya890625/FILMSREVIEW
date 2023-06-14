import httpx
import json
from pathlib import Path

MEDIA_DIR = Path(__file__).resolve().parent.parent / "moviereviews" / "media" / "movie"/ "images"  # noqa E501
SERVER = "http://localhost:8000"


def test_get_home_page() -> None:
    url: str = f"{SERVER}/home/"
    resp: httpx = httpx.get(url)
    assert resp.status_code == 200


def test_signup_form() -> None:
    url: str = f"{SERVER}/accounts/signupaccount/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    with httpx.Client() as client:
        user_data = {
            "username": "user1",
            "password1": "password1",
            "password2": "password1",
        }
        resp = client.post(url=url, data=user_data)
        resp.status_code = 302


def test_user_behavior_client() -> None:
    url: str = f"{SERVER}/home/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    # CREATE MOVIE
    new_movie_data = {
        "title": "movie1",
        "description": "opus mupus",
    }
    new_movie_image = {
        "image": open(f"{MEDIA_DIR_FILE}", 'rb') # noqa E501
    }
    resp = httpx.post(url=f"{SERVER}/movie/create/", data=new_movie_data, files=new_movie_image) # noqa E501
    movie_id = json.loads(resp.text).get('id')
    assert resp.status_code == 201
    # USER LOGINS
    url = f"{SERVER}/accounts/login/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    user_data = {
        "username": "user1",
        "password": "password1"
    }
    resp = httpx.post(url=url, data=user_data)
    resp.status_code = 302
    session_id = resp.cookies["sessionid"]
    headers = {"Cookie": f"sessionid={session_id}"}
    with httpx.Client(headers=headers) as client:
        # USER VISITS PARTICULAR MOVIE
        url = f"{SERVER}/{movie_id}"
        resp = client.get(url)
        assert resp.status_code == 200
        # USER WANTS TO ADD REVIEW
        url = f"{SERVER}/{movie_id}/create"
        resp = client.get(url)
        assert resp.status_code == 200


def test_movie_crud() -> None:
    # READ ALL MOVIES
    url_get: str = f"{SERVER}/movies/"
    resp = httpx.get(url_get)
    assert resp.status_code == 200
    # CREATE NEW MOVIE
    new_movie_data = {
        "title": "movie1",
        "description": "opus mupus",
    }
    movie_image = MEDIA_DIR / "back-to-the-future_poster.jpg"
    new_movie_image = {
        "image": open(f"{movie_image}", 'rb')
    }
    resp = httpx.post(url=f"{SERVER}/movie/create/", data=new_movie_data, files=new_movie_image) # noqa E501
    assert resp.status_code == 201
    # GET MOVIE ID
    movie_id = json.loads(resp.text).get('id')
    # READ ONE MOVIE
    url = f"{SERVER}/movie/{movie_id}/detail/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    # UPDATE MOVIE
    update_movie_data = {
        "title": "movie1",
        "description": "opus mupus",
    }
    movie_image = MEDIA_DIR / "2001_A_Space_Odyssey_1968.png"
    update_movie_image = {
        "image": open(f"{movie_image}", 'rb')
    }
    resp = httpx.put(url=f"{SERVER}/movie/{movie_id}/update/", data=update_movie_data, files=update_movie_image) # noqa E501
    assert resp.status_code == 200
    # DELETE MOVIE
    url: str = f"{SERVER}/movie/{movie_id}/delete/"
    resp = httpx.delete(url)
    assert resp.status_code == 204
