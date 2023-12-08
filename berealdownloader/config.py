import yaml

config = None


def load_config():
    global config
    with open("config.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)


def get_config():
    global config

    if not config:
        load_config()

    return config


def get_token():
    config = get_config()
    if "token" not in config:
        raise EnvironmentError("No token found in config.yaml")

    return config["token"]
