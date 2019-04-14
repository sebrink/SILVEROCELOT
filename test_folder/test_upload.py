import requests

def test_1_upload_link():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    params = {'fileinlink':'https://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4', 'videoname':'MEEP', 'filein':' '}
    page = requests.get('https://localhost/python/upload.py', params=params, cookies=cookies, verify=False)
    assert 'File downloaded' in page.text

def test_2_delete():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    params = {'video':'MEEP'}
    page = requests.get('https://localhost/python/delete.py', params=params, cookies=cookies, verify=False)
    assert '/html/manage.html' in page.text


def test_3_delete_novideo():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    params = {'video':'FAKE'}
    page = requests.get('https://localhost/python/delete.py', params=params, cookies=cookies, verify=False)
    assert '/html/manage.html' in page.text
