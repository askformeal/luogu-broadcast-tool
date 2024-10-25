import requests
from bs4 import BeautifulSoup
import json
import pyperclip

cookie = '__client_id=627f4c1bf139fa5ef97dab418b44481b3c60cdd1;_uid=787042;C3VK=3c2971'
headers = {'User-Agent': 
           'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0',}

team_id = int(input('输入团队id: '))
html = requests.get(f"https://www.luogu.com.cn/api/team/members/{team_id}", headers = headers).text

bs = BeautifulSoup(html, 'html.parser')

results = json.loads(bs.text)["members"]["result"]

at_list = ''

for result in results:
    user = result["user"]
    at_list += f'@{user['name']} \n\n'

print(at_list)

pyperclip.copy(at_list)
print("已复制到剪贴板")

