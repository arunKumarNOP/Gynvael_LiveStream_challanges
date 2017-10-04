import urllib
import requests

base64enc = urllib.unquote('6VhhU05LYPoyhOCajJ9mZw%2BdSO1%2FAj4%3D')
t = base64enc.decode('base64')

s = '{"access_level":"user"}'
link = 'http://gynvael.coldwind.pl/b8263ba523af6ebd992e3782e9edd99fbdad4203_mission017'

for a in range(0xff):
    l = bytearray(t)
    l.append(a)

    for i in range(6):
        l[17+i] = l[17+i]^ord(s[i+17])^ord('admin"'[i])

    base64encoded = str(l).encode('base64')
    print a, '->', urllib.quote(base64encoded)
    cookie = {'mission017session': urllib.quote(base64encoded)}
    response = requests.get(link, cookies=cookie).text
    if 'Have a new cookie' not in response:
    	print response
    	break