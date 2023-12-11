import json
f1 = open('xxt.json')
cookie = f1.read()
cookie = json.loads(cookie)
print(cookie)
