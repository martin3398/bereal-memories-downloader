import io
import os
from collections import defaultdict

import requests
from PIL import Image


def save_all(memory_metadata: dict, save_path: str):
    dates_count = defaultdict(int)

    for memory in memory_metadata:
        date = memory["date"]
        count = dates_count[date]
        dates_count[date] += 1

        memory_path = os.path.join(save_path, date)
        primary_path = os.path.join(memory_path, f"{count}_primary.png")
        secondary_path = os.path.join(memory_path, f"{count}_secondary.png")

        if not os.path.exists(memory_path):
            os.makedirs(memory_path)

            download_memory(memory["primary"], primary_path)
            download_memory(memory["secondary"], secondary_path)

            print(f"Downloaded memory {count + 1} from {date}")
        else:
            print(f"Memory {count + 1} from {date} already exists")


def download_memory(url: str, path: str):
    response = requests.get(url)

    image = Image.open(io.BytesIO(response.content))
    image.save(path, "PNG")
