import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入需要翻译的内容（输入"q!"退出 程序）：')
    if content == 'q!':
        break

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    '''
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] =  'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15655150400976'
    data['sign'] = 'be0519003d792e6ef5dd6c9cbcc0a0db'
    data['ts'] = '1565515040097'
    data['bv'] = '7e3150ecbdf9de52dc355751b074cf60'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')

    # req = urllib.request.Request(url, data, head)
    req = urllib.request.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']
    print("翻译结果:%s" % target)
    time.sleep(5)
