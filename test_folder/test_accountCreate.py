import requests

def test_newAccount_input():
    params = {'username':'new', 'password':'new', 'displayName':'new'}
    page = requests.get('https://localhost/python/newAccount.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'User Created' in page.text

def test_newAccount_user_exists():
    params = {'username':'new', 'password':'new', 'displayName':'new'}
    page = requests.get('https://localhost/python/newAccount.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'Already Exists' in page.text
