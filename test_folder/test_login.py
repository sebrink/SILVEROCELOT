import requests

def test_login_good_input():
    params = {'username':'new', 'password':'new', 'recap':'L33THAx0rTest'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'Failed' not in page.text

def test_login_noAccount():
    params = {'username':'fake', 'password':'fake', 'recap':'L33THAx0rTest'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'Failed' in page.text

def test_login_bad_captcha():
    params = {'username':'new', 'password':'new', 'recap':'xdddd'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    assert 'Recaptcha Failed' in page.text
