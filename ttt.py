# *--conding:utf-8--*

data="private-Session.1 {'message': {'id': 167, 'uid': 8, 'session_id': 1, 'type': 1, 'content': '的', 'read_at': None, 'created_at': '2019-07-03 07:57:01', 'updated_at': '2019-07-03 07:57:01'}, 'socket': None}"
import re

data=re.findall("'content': '(.*?)',",data)[0]
uid = re.findall("'uid':(.*),",data)
print(data)
print(uid)