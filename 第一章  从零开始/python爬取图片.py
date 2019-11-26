import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def get_image(html):
    p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    imglist = re.findall(p, html)
    num = 1
    for each in imglist:
        # 读取图片数据
        response = urllib.request.urlopen(each)
        image = response.read()  # 不能进行'utf-8'编码,不能调用open_url()函数

        with open('%s.jpg' % num, 'wb') as fp:
            fp.write(image)
            print("正在下载第%s张图片" % num)
            num = num + 1
    return

url = "https://tieba.baidu.com/p/5316245951"
get_image(open_url(url))