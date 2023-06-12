import httpx
import json


SERVER = "http://localhost:8000"


def test_get() -> None:
    url: str = f"{SERVER}/home/"
    resp: httpx = httpx.get(url)
    assert resp.status_code == 200


def test_signup_form() -> None:
    url: str = f"{SERVER}/accounts/signupaccount/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    user_data = {
        "username": "user3",
        "password": "password3",
        "password2": "password3",
    }
    resp = httpx.post(url=url, data=user_data)
    resp.status_code = 302

def test_user_behavior_client() -> None:
    url: str = f"{SERVER}/home/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    # USER LOGINS
    url: str = f"{SERVER}/accounts/login/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    user_data = {
            "username": "user3",
            "password": "password3"
        }

    resp = httpx.post(url=url, data=user_data)
    resp.status_code = 302
    session_id = resp.cookies["sessionid"]
    headers = {"Cookie": f"sessionid={session_id}"}
    with httpx.Client(headers=headers) as client:
        # USER VISITS PARTICULAR MOVIE
        url = f"{SERVER}/23c30cd3-49e8-433a-a460-0aed26f0a92a"
        resp = client.get(url)
        assert resp.status_code == 200
        # USER WANTS TO ADD REVIEW
        url = f"{SERVER}/23c30cd3-49e8-433a-a460-0aed26f0a92a/create"
        resp = client.get(url)
        assert resp.status_code == 200
# def test_user_behavior() -> None:
#     # USER VISITS HOMEPAGE
#     url: str = f"{SERVER}/home/"
#     resp = httpx.get(url)
#     assert resp.status_code == 200
#     # USER LOGINS
#     url: str = f"{SERVER}/accounts/login/"
#     resp = httpx.get(url)
#     assert resp.status_code == 200
#     user_data = {
#         "username": "user3",
#         "password": "password3"
#              }
#     resp = httpx.post(url=url, data=user_data)
#     resp.status_code = 302
#     session_id = resp.cookies["sessionid"]
#     # USER VISITS PARTICULAR MOVIE
#     url = f"{SERVER}/23c30cd3-49e8-433a-a460-0aed26f0a92a"
#     resp = httpx.get(url, headers={"Cookie": f"sessionid={session_id}"})
#     assert resp.status_code == 200
#     # USER WANTS TO ADD REVIEW
#     url = f"{SERVER}/23c30cd3-49e8-433a-a460-0aed26f0a92a/create"
#     resp = httpx.get(url, headers={"Cookie": f"sessionid={session_id}"})
#     assert resp.status_code == 200


def test_movie_crud() -> None:
    url_get: str = f"{SERVER}/movies/"
    resp = httpx.get(url_get)
    assert resp.status_code == 200
    new_movie_data = {
        "title": "movie1",
        "description": "opus mupus",
    }
    new_movie_image = {
        "image": open("C:/Users/Митя/Desktop/POSTERS_ФИЛЬМЫ/back-to-the-future_poster.jpg", 'rb') # noqa E501
    }
    resp = httpx.post(url=f"{SERVER}/movie/create/", data=new_movie_data, files=new_movie_image) # noqa E501
    assert resp.status_code == 201
    movie_id = json.loads(resp.text).get('id')
    url: str = f"{SERVER}/movie/{movie_id}/delete/"
    resp = httpx.delete(url)
    assert resp.status_code == 204


def test_get_review() -> None:
    url: str = f"{SERVER}/accounts/login/"
    resp = httpx.get(url)
    assert resp.status_code == 200
    user_data = {
        "username": "user3",
        "password": "password3"
    }
    resp = httpx.post(url=url, data=user_data)
    resp.status_code = 302
