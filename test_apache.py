import urllib.request

def test_hello_world():
	page = urllib.request.urlopen('http://localhost:80').read().decode("utf-8")
	assert 'Hello world' in page
