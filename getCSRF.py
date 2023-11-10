import json
import webbrowser
import requests
from bs4 import BeautifulSoup

# def bypassCSRF():
#     LOGIN_URL = 'https://accounts.teky.edu.vn/users/sign_in?locale=vi'
#     headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml',
#         'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
#     }

#     response = requests.get(LOGIN_URL, headers=headers, verify=False)

#     soup = BeautifulSoup(response.text, 'lxml')

#     csrf_token = soup.select_one('meta[name="csrf-token"]')['content']

#     print(csrf_token)
    
#     return csrf_token

LOGIN_URL = 'https://accounts.teky.edu.vn/users/sign_in?locale=vi'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

response = requests.get(LOGIN_URL, headers=headers, verify=False)

soup = BeautifulSoup(response.text, 'lxml')

csrf_token = soup.select_one('meta[name="csrf-token"]')['content']

payload = {
        "authenticity_token": str(csrf_token),
        "user%5Bemail%5D": "84913760666",
        "user%5Bpassword%5D": "%09Teky%402023",
        "commit": "%C4%90%C4%83ng+nh%E1%BA%ADp"
    }

response = requests.post(LOGIN_URL, data=json.dumps(payload), headers=headers)

y = response.text
f = open("error.html", "a")
f.write(y)
f.close()
webbrowser.open_new_tab('error.html')