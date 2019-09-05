import urllib.request
import re

def open_url(url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
        page = urllib.request.urlopen(req)
        html = page.read().decode('utf-8')

        return html

def get_img(html):
    p = r'<img class = "BDE_Image" src="([^"]+\.jag)"'
    imglist = re.findall(p,html)
    '''
    for each in imglist:
        print(each)
    '''
    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)

if __name__ == '__main__':
    url = "https://tieba.baidu.com/p/6224707677"
    get_img(open_url(url))