# 安装aip  pip install baidu-aip
import os
from aip import AipOcr

print("识别身份证速度较慢，请耐心等待".center(60))
APP_ID = '16296141'
API_KEY = 'Mp0OGTUKUdwaPC7u4uMOXG9Z'
SECRET_KEY = 'YFgfrVUrfGOT00M5jFoWowGP8gVn4voY'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

BASE_DIR = os.getcwd()
id_list = os.listdir(os.path.join(BASE_DIR, "要识别的身份证"))
success_path = os.path.join(BASE_DIR, "successful.txt")
count = 0
for id in id_list:
    img = open(os.path.join(BASE_DIR, "要识别的身份证", id), 'rb').read()
    msg = client.basicGeneral(img)  # 识别图片
    str1 = ""
    for i in msg["words_result"]:
        print("{}".format(i["words"]).center(60))
        str1 += "{}\n".format(i["words"])
    with open(success_path, 'a') as f:
        f.write("{}\n\n".format(str1))
        print("\n")
    print("写入中，请稍等。。。".center(60))
    count+=1
    print("\n\n")
print("执行结束，共完成了{}个身份证的识别，资料已写入到successful.txt".format(count).center(60))
ss = input("")