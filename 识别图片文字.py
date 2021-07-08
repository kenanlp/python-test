from aip import AipOcr
import re
import os
import time
APP_ID = '21576896'
API_KEY = 'OINC7DFnjne4fc3ffS642cbg'
SECRET_KEY = 'GGl8lTjXTKgrskbveKNX913lNyfQCpGB'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 把读出的文字内容统一保存在一个txt文档里
f = open(r'./plateread.txt', 'w')

# 保存了待识别图片的路径
PlatePath = r'./pic'

# 按顺序识别出图片，并把图片文件名改成“识别出的文字.jpg”的格式
for Dir in os.listdir(PlatePath):
    srcDir = os.path.join(PlatePath, Dir)
    # print(srcDir)
    fsrc = open(srcDir, 'rb')

    img = fsrc.read()

    message = client.basicAccurate(img)

    for results in message.get('words_result'):
        name = results.get('words')
        print(name)
        f.write(name)
        # dstDir = os.path.join(r'./pic', name) + '.png'
        # # print(dstDir)
        # fsrc.close()
        # os.rename(srcDir, dstDir)

    time.sleep(0.3)
f.close()