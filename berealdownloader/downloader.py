from berealdownloader import config, memory_saver
from berealdownloader.api import login, memories


def download():
    jwt = config.get_jwt()
    save_path = config.get_save_path()

    access_token = login.get_access_token(jwt)

    memory_metadata = memories.get_memories_data(access_token)

    memory_saver.save_all(memory_metadata, save_path)
