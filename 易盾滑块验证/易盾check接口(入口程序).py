import json
import requests

from 易盾get接口 import get_cb
from 计算距离 import get_distance
from 易盾check接口 import get_check_params, get_cb_value, get_callback

cookies = {
    '_ga': 'GA.1.2df4a2e609326.078712ff1bb7508b29ed',
    '_ntes_nnid': '2d031ee66c4c009a0a8fcc9b690e92e0,1790230238777',
    '_ntes_nuid': '2d031ee66c4c009a0a8fcc9b690e92e0',
    'hb_MA-93D5-9AD06EA4329A_source': 'www.baidu.com',
    'Hm_lvt_4671c5d502135636b837050ec6d716ce': '1792142779,1792236988,1792259788',
    'HMACCOUNT': '45D5E8B3A406A03A',
    'Hm_lpvt_4671c5d502135636b837050ec6d716ce': '1792259796',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://dun.163.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': '_ga=GA.1.2df4a2e609326.078712ff1bb7508b29ed; _ntes_nnid=2d031ee66c4c009a0a8fcc9b690e92e0,1790230238777; _ntes_nuid=2d031ee66c4c009a0a8fcc9b690e92e0; hb_MA-93D5-9AD06EA4329A_source=www.baidu.com; Hm_lvt_4671c5d502135636b837050ec6d716ce=1792142779,1792236988,1792259788; HMACCOUNT=45D5E8B3A406A03A; Hm_lpvt_4671c5d502135636b837050ec6d716ce=1792259796',
}

# ① get 那一次：token + 两张图
info = get_cb()
token = info['token']

# ② 同一张图算位移（300 宽度基准）
slide = get_distance(info, display_width=300)

# ③ d / m / p / f / ext
data = get_check_params(token, slide)

# ④ cb 分两次调用：check 这次重新算一个
cb = get_cb_value()

# ⑤ JSONP callback 名，由 JS 的 get_callback() 生成
callback = get_callback()

params = {
    'referer': 'https://dun.163.com/trial/sense',
    'zoneId': 'CN31',
    'dt': 'mU2JPlNylThAVwQFFAaYF3VxFcOqeoCM',
    'id': '5a0e2d04ffa44caba3f740e6a8b0fa84',
    'token': token,
    'data': json.dumps(data, separators=(',', ':')),
    'width': '300',
    'type': '2',
    'version': '2.28.5',
    'cb': cb,
    'user': '',
    'extraData': '',
    'bf': '0',
    'runEnv': '10',
    'sdkVersion': '',
    'loadVersion': '2.5.4',
    'iv': '4',
    'callback': callback,
}

response = requests.get('https://c.dun.163.com/api/v3/check', params=params, cookies=cookies, headers=headers, timeout=10)

print('slide   =', slide)
print('callback=', callback)
print(response.text)
payload = json.loads(response.text[response.text.index('(') + 1:response.text.rindex(')')])
print('error:', payload.get('error'), 'msg:', payload.get('msg'))
