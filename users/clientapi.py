from asyncio.windows_events import NULL
import requests
import json
from random import randint

BASE_URL = "https://go.teachbase.ru/"
CLIENT_ID = "VPn6dJBPKYLhTzC7sASXLUnrrE6NlggnDCX8B_0RR3Y"
CLIENT_SECRET = "lKLWRP30INSj-dUz7hZspLV7BOOw79Hl1k0GnpdD5vY"
GRANT_TYPE = "client_credentials"


def gettoken(resource_uri="/oauth/token"):
    PARAMS = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": GRANT_TYPE,
    }
    url = "{0}{1}".format(BASE_URL, resource_uri)
    response = requests.post(url, params=PARAMS)

    if response.status_code == 200:
        return json.loads(response.text)["access_token"]
    return response.status_code


def getcourses(resource_uri="/endpoint/v1/courses", page=1, per_page=10):
    PARAMS = {
        "access_token": gettoken(),
        "page": page,
        "per_page": per_page,
    }
    url = "{0}{1}".format(BASE_URL, resource_uri)
    response = requests.get(url, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    return response.status_code


def getcoursedetail(
    resource_uri="/endpoint/v1/courses/", courseid="", page=1, per_page=10
):
    PARAMS = {
        "access_token": gettoken(),
        "page": page,
        "per_page": per_page,
    }
    url = "{0}{1}{2}".format(BASE_URL, resource_uri, courseid)
    response = requests.get(url, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    return response.status_code


def getcoursesessions(
    resource_uri="/endpoint/v1/courses/",
    courseid="",
):
    PARAMS = {
        "access_token": gettoken(),
    }
    url = "{0}{1}{2}/course_sessions".format(BASE_URL, resource_uri, courseid)
    response = requests.get(url, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    return response.status_code


def sessionregister(sessionid="", email=NULL, phone=NULL, user_id=""):
    PARAMS = {
        "access_token": gettoken(),
    }
    data = {
        "email": email,
        "phone": phone,
        "user_id": user_id,
    }
    url = "{0}/endpoint/v1/course_sessions/{1}/register".format(
        BASE_URL, sessionid
    )
    response = requests.post(url, params=PARAMS, json=data)
    return response.status_code, json.loads(response.text)


def userregister(email=NULL, name="", lastname="", phone=NULL):
    PARAMS = {
        "access_token": gettoken(),
    }
    data = {
        "users": [
            {
                "email": email,
                "name": name,
                "description": "some description",
                "last_name": lastname,
                "phone": phone,
                "role_id": 1,
                "auth_type": 0,
                "external_id": ("fd-" + str(randint(1001, 9999))),
                "labels": {"1": "2", "3": "4"},
                "password": "qwerty",
                "lang": "ru",
            }
        ],
        "options": {
            "activate": True,
            "verify_emails": False,
            "skip_notify_new_users": True,
            "skip_notify_active_users": True,
        },
        "external_labels": True,
    }
    resource_uri = "/endpoint/v1/users/create"
    url = "{0}{1}".format(BASE_URL, resource_uri)
    response = requests.post(url, params=PARAMS, json=data)
    if response.status_code == 200:
        return response.status_code, json.loads(response.text)[0]
    return response.status_code, response.text

if __name__=="__main__":
    print(getcourses()[0].get("id"))
