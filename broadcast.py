import requests
import json
import pyperclip
import os
import sys

headers = {'User-Agent': 
           'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0',}
print('洛谷团队群发机，demons1014出品')

if (len(sys.argv) > 1):
    try:
        team_id = int(sys.argv[1])
    except ValueError:
        print("参数错误")
        sys.exit()
else:
    team_id = int(input('输入团队id: '))
html = requests.get(f"https://www.luogu.com.cn/api/team/members/{team_id}", headers = headers).text

results = json.loads(html)["members"]["result"]

'''with open('tmp.json', 'w', encoding="utf-8") as f: #调试代码
    #tmp = str(json.loads(html))
    tmp = str(html)
    #tmp.encode('utf-8')
    f.write(tmp)'''

at_list = []

for result in results:
    user = result["user"]
    at_list.append(f'@[{user["name"]}](luogu://user/{user['uid']}) \n\n')

output = ""
step = 5

for i in range(0,len(at_list), step):

    tmp = ''
    cnt = len(at_list[i:i+step])
    for user in at_list[i:i+step]:
        tmp += user
        print(user, end='')
    pyperclip.copy(tmp)
    print(f"已将{cnt}个用户名复制到剪贴板")
    os.system('pause')
print('所有用户名已输出完毕，感谢您使用本软件')