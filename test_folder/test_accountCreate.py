import requests

def test_newAccount_input():
    params = {'username':'new', 'password':'new', 'displayName':'new', 'recap':'L33THAx0rTest'}
    page = requests.get('https://localhost/python/newAccount.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'User Created' in page.text

def test_newAccount_user_exists():
    params = {'username':'new', 'password':'new', 'displayName':'new', 'recap':'L33THAx0rTest'}
    page = requests.get('https://localhost/python/newAccount.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'Already Exists' in page.text

def test_newAccount_bad_captcha():
    params = {'username':'new', 'password':'new', 'displayName':'new', 'recap':'xdddd'}
    page = requests.get('https://localhost/python/newAccount.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'Recaptcha Failed' in page.text
