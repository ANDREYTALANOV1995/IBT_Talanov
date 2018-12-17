import re
import requests

url = 'http://fan.lib.ru/'

s_fan1 = requests.get(url)

result = re.findall(r'<a href=.*?a>', s_fan1.text)

res = [s for s in result if "Фэнтези" in s]

res = re.findall(r'\/.*shtml', res[0])

s_fan2 = requests.get(url+res[0])

result2 = re.findall(r'\/\S*shtml', s_fan2.text)

for re in result2:
    print(url+re)