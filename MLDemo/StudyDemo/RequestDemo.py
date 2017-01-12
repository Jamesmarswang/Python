# coding = utf-8
# author = 'wang wei'


import requests


def use_simple_requests():
    url = 'www.baidu.com'
    response = requests.get(url)
    print(response.headers)
    print(response.text)
    print('====================')
    params = {'param1': 'hello', 'param2': 'world'}
    response2 = requests.get(url, params=params)
    print(response2.text)


if __name__ == '__main__':
    use_simple_requests()
