import requests

def test_upload():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    params = {'fileinlink':'https://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4', 'videoname':'MEEP', 'filein':' '}
    page = requests.get('https://localhost/python/upload.py', params=params, cookies=cookies, verify=False)
    assert 'File downloaded' in page.text
