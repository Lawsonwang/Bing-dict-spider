import urllib.request
import re
import os
os.system("color f9")
word = input('请输入要查询的英语单词：')
print("查询中……")
response = urllib.request.urlopen("https://cn.bing.com/dict/search?q=" + word)
html = response.read().decode('utf-8')
#with open("bing.txt", "w", encoding="utf-8") as file:
#    file.write(html)
rep = re.compile(r'class="pos">(.+?)</span><span\ class="def\ b_regtxt"><span>(.+?)</span>')
findlist = rep.findall(html)
rep2 = re.compile(r'class="pos\ web">(网络)</span><span\ class="def\ b_regtxt"><span>(.+?)</span>')
findlist2 = rep2.findall(html)
os.system("cls")
print(word)
for each in findlist:
    print(each[0], each[1])
for each in findlist2:
    print(each[0], each[1])
#rep3 = re.compile(r'class="pos.*?">(.+?)</span><span\ class="def\ b_regtxt"><span>(.+?)</span>')
if (findlist == []) and (findlist2 == []):
    print("无搜索结果！")
input()
