import requests

def test_logout():
    params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    page = requests.get('https://localhost/python/logout.py', cookies=cookies, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    page = requests.get('https://localhost', cookies=cookies, verify=False)
    assert 'Welcome' in page.text
