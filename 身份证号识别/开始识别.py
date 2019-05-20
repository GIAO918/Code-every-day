# 安装aip  pip install baidu-aip
import os
from aip import AipOcr

APP_ID = '16296141'
API_KEY = 'Mp0OGTUKUdwaPC7u4uMOXG9Z'
SECRET_KEY = 'YFgfrVUrfGOT00M5jFoWowGP8gVn4voY'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

BASE_DIR = os.getcwd()
id_path = os.path.join(BASE_DIR, "要识别的身份证")
id_list = os.listdir(id_path)

success_path = os.path.join(BASE_DIR, "successful.txt")
for id in id_list:
    img = open(os.path.join(BASE_DIR, "要识别的身份证", id), 'rb').read()
    msg = client.basicGeneral(img)  # 识别图片

    for i in msg["words_result"]:
        print(i["words"])
        with open(success_path, 'a') as f:
            f.write("{}\n\n".format(i["words"]))
