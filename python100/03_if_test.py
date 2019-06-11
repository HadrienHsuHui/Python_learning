"""
身份认证
"""

username = input('pls input user name')
password = input('pls input password')

if username == 'admin' and password == '123456':
    print('login ok')
else:
    print('login fail')
