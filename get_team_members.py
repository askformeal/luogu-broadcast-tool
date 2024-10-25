import requests
import json
import pyperclip

cookie = '__client_id=627f4c1bf139fa5ef97dab418b44481b3c60cdd1;_uid=787042;C3VK=3c2971'
headers = {'User-Agent': 
           'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0',}
print('洛谷团队群发机，demons1014出品')
team_id = int(input('输入团队id: '))
html = requests.get(f"https://www.luogu.com.cn/api/team/members/{team_id}", headers = headers).text

results = json.loads(html)["members"]["result"]

at_list = []

for result in results:
    user = result["user"]
    at_list.append(f'@{user['name']} \n\n')

step = 5

for i in range(0,len(at_list), step):

    tmp = ''
    cnt = len(at_list[i:i+step])
    for user in at_list[i:i+step]:
        tmp += user
        print(user, end='')
    pyperclip.copy(tmp)
    input(f"已将{cnt}个用户名复制到剪贴板，发送后请按回车……")
print('所有用户名已输出完毕，感谢您使用本软件')