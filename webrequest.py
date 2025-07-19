import requests

url = "https://google.com"


for str in ["a", "b", "c", "d"]:
    res = requests.post(
        url,
        params={"debug": "1"},  # 쿼리스트링
        headers={"User-Agent": "/1.0"},
        cookies={"session": "abc123"},
        data={"username": f"{str}", "password": "1234"},
        timeout=5,
    )


print(res.status_code, res.text)
