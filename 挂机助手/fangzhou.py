# coding=utf-8
"""
方舟自动刷图工具，使用前把游戏调整到 游击演戏界面
"""
import time
import autopy
import random

count = 1
while True:
    print("自动化刷图第{}轮".format(count))
    autopy.mouse.smooth_move(1839, 400)  # 坐标定位开始行动的图标
    time.sleep(random.randint(5, 10))

    autopy.mouse.click()  # 单击
    time.sleep(random.randint(1, 10))

    autopy.mouse.smooth_move(1818, 328)
    autopy.mouse.click()

    time.sleep(random.randint(100, 150))  # 等待刷完

    autopy.mouse.smooth_move(1839, 400)  # 点任意位置，返回初始刷图页面
    autopy.mouse.click()

    time.sleep(random.randint(8, 20))  # 等待页面响应
    count += 1
