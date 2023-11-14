import requests
import json
import webbrowser
import os
from bs4 import BeautifulSoup

class ResponseVerbose(requests.Response):
    extra_header_repr = 'X-Request-Id'

    def __repr__(self):
        return '<Response [{}] {}: {}>'.format(
            self.status_code,
            self.extra_header_repr,
            self.headers.get(self.extra_header_repr, 'None')
        )


class Session(requests.Session):
    def __init__(self):
        super().__init__()

        self.hooks['response'] = self.build_response

    @staticmethod
    def build_response(resp, *args, **kwargs):
        """
        Let's rebuild the source response into required verbose response object using all fields from the original

        FYI: requests.adapters.HTTPAdapter.build_response
        """
        response = ResponseVerbose()
        response.status_code = resp.status_code
        response.headers = resp.headers
        response.encoding = resp.encoding
        response.raw = resp.raw
        response.reason = response.raw.reason
        response.url = resp.url
        response.cookies = resp.cookies.copy()
        response.request = resp.request
        response.connection = resp.connection

        return response


def main():
    url = 'https://accounts.teky.edu.vn/users/sign_in'

    sess = Session()
    print('response using our own session object: {}'.format(sess.get(url)))

    
    
    LOGIN_URL = 'https://accounts.teky.edu.vn/users/sign_in'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    response = sess.get(LOGIN_URL, headers=headers, verify=False)

    soup = BeautifulSoup(response.text, 'lxml')

    open('login.html', 'w').close()
    y = response.content
    with open('login.html', "wb") as f:
        f.write(y)
    f.close()
    webbrowser.open_new_tab('login.html')

    csrf_token = soup.select_one('meta[name="csrf-token"]')['content']
    cokies = response.cookies
    print(cokies)
    headers = {
        "authority":"accounts.teky.edu.vn",
        "Content-Type": "application/x-www-form-urlencoded",   
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }

    payload = {
            "authenticity_token": str(csrf_token),
            "user%5Bemail%5D": "84913760666",
            "user%5Bpassword%5D": "%09Teky%402023",
            "commit": "%C4%90%C4%83ng+nh%E1%BA%ADp"
        }
    LOGIN_URL = 'https://accounts.teky.edu.vn/users/sign_in?locale=vi'
    response = sess.post(LOGIN_URL, data=json.dumps(payload), headers=headers, cookies=cokies)
    
    print(response.status_code)
    open('error.html', 'w').close()
    y = response.text
    f = open("error.html", "a")
    f.write(y)
    f.close()
    webbrowser.open_new_tab('error.html')


if __name__ == '__main__':
    main()