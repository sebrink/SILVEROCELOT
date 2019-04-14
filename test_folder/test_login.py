import requests

def test_login_good_input():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'Failed' not in page.text

def test_login_noAccount():
    params = {'username':'fake', 'password':'fake'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'Failed' in page.text
