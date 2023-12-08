from berealdownloader import config
from berealdownloader.api import login


def download():
    jwt = config.get_jwt()

    access_token = login.get_access_token(jwt)
