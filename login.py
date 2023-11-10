
import json
import webbrowser
import requests
import getCSRF

def main():
    url = "https://accounts.teky.edu.vn/users/sign_in?locale=vi"

    headers = {'content-type': 'application/json','accept': 'text/html,application/xhtml+xml,application/xml',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    # Example echo method
    payload = {
        "authenticity_token": str(getCSRF.bypassCSRF),
        "user%5Bemail%5D": "84913760666",
        "user%5Bpassword%5D": "%09Teky%402023",
        "commit": "%C4%90%C4%83ng+nh%E1%BA%ADp"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    y = response.text
    f = open("error.html", "a")
    f.write(y)
    f.close()
    webbrowser.open('file:///root/python/home.html')


if __name__ == "__main__":
    main()