"""
pip install requests
pip install xlrd
pip install xlwt
"""

import requests
import json
import xlrd
import xlwt

# 第三方接口获得的KEY值，充钱获得
key = '7huTJVRoBH18QZ6iW1OdVpmBaU1khiC3'

# 打开excel文件
data = xlrd.open_workbook(r"{}\666.xlsx".format(r'C:\Users\Administrator\Desktop\道琼斯+Ravenpack 数据源交集.xlsx'))
sheet1 = data.sheet_by_name('Sheet1')  # 这里写要排序的sheet
# 进入sheet 获取到这一列的数据，第2列的第一行到50行
name_list = sheet1.col_values(0, 1, 500)

# 定义两个列表，一个接收识别失败的url，一个接收识别成功的url
error_list = []
success_list = []

# 循环表格中选定的那一列的数据，每个url做识别。并加入对应结果的列表中
for name in name_list:
    r = requests.get('http://api.alexa.cn/alexa/general?site={}&key={}'.format(name, key))
    result = json.loads(r.text)
    if result["error_code"] == 0:
        success_list.append(result)
    else:
        error_list.append(name)

print(success_list)
print(error_list)
# 对成功识别的列表中的数据进行排序
pv_rank = sorted(success_list, key=lambda x: int(x["result"]["world_pv_rank"]))  # 按照全球排名得到的列表
uv_rank = sorted(success_list, key=lambda x: int(x["result"]["world_uv_rank"]))  # 按照访客排名得到的列表
country_rank = sorted(success_list, key=lambda x: int(x["result"]["country_rank"]))  # 国家地区排名

# 把排序后的排名写入到excel
workbook = xlwt.Workbook(encoding="utf-8")  # 新建一个excel 表格
worksheet = workbook.add_sheet("sheet1")  # 表格里边新建一个sheet
worksheet.write(0, 0, label='全球排名')  # 往sheet里边的label插入数据
worksheet.write(0, 1, label='访客排名')
worksheet.write(0, 2, label='地区排名')

count = 1
for i in pv_rank:
    worksheet.write(count, 0, label=i["result"]["domain"])
    count += 1
count = 1
for i in uv_rank:
    worksheet.write(count, 1, label=i["result"]["domain"])
    count += 1
count = 1
for i in country_rank:
    worksheet.write(count, 2, label=i["result"]["domain"])
    count += 1
workbook.save('Excel_test666.xlsx')  # 保存操作
