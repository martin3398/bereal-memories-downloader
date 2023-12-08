from datetime import datetime, timedelta

import jwt
import requests


def refresh_access_token(refresh_token: str):
    url = "https://auth.bereal.team/token"
    params = {
        "grant_type": "refresh_token"
    }
    body = {
        "grant_type": "refresh_token",
        "client_id": "ios",
        "client_secret": "962D357B-B134-4AB6-8F53-BEA2B7255420",
        "refresh_token": refresh_token
    }

    response = requests.post(url, params=params, json=body)
    if response.status_code != 201:
        raise Exception("Could not refresh token")

    return response.json()["access_token"]


def get_access_token(jwt_content: str):
    jwt_data = jwt.decode(jwt_content, options={"verify_signature": False}, algorithms=["HS256"])

    access_token = jwt_data["access"]["token"]
    expires = datetime.fromisoformat(jwt_data["access"]["expires"])  #
    now = datetime.now(expires.tzinfo)

    if now + timedelta(hours=1) > expires:
        access_token = refresh_access_token(jwt_data["access"]["refresh_token"])

    return access_token
