import requests


def get_memories_data(access_token: str):
    url = "https://mobile.bereal.com/api/feeds/memories"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Could not get mmories")

    json_data = response.json()
    data = []
    for memory in json_data["data"]:
        data.append({
            "date": memory["memoryDay"],
            "primary": memory["primary"]["url"],
            "secondary": memory["secondary"]["url"]
        })

    return data
