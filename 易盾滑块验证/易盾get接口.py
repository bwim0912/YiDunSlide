import requests,execjs
import json

def get_cb():
    json_str=open('get_cb.js',mode='r',encoding='utf-8').read()
    cb=execjs.compile(json_str).call('get_cb')
    cookies = {
        '_ga': 'GA.1.2245a834c5932.6889df2b106d1980e6e9',
        '_ntes_nnid': '2d031ee66c4c009a0a8fcc9b690e92e0,1790230238777',
        '_ntes_nuid': '2d031ee66c4c009a0a8fcc9b690e92e0',
        'hb_MA-93D5-9AD06EA4329A_source': 'www.baidu.com',
        'Hm_lvt_4671c5d502135636b837050ec6d716ce': '1792142779,1792236988',
        'HMACCOUNT': '45D5E8B3A406A03A',
        'Hm_lpvt_4671c5d502135636b837050ec6d716ce': '1792237000',
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
    }

    params = {
        'referer': 'https://dun.163.com/trial/sense',
        'zoneId': 'CN31',
        'dt': 'mU2JPlNylThAVwQFFAaYF3VxFcOqeoCM',
        'irToken': 'rAAWpOVSiIZBM1REQRLcByHGmTyDZKxu',
        'id': '5a0e2d04ffa44caba3f740e6a8b0fa84',
        'fp': 'ESWrZocOQe6kWrs5NZ2tMaCDfpYGemjEDt7Ewnetl+CBxaXd\\2zkeNjSEuXMC+GoBwo71BdG+56lTmlE640XBOwRxM\\0ydiY\\kTqSAnw2gnlEReXqWfvyLjrRultccN6S1Qyzohu+QizymmPS\\ontPioShANteegL22Gs\\9x7NE3WOcu:1792237901044',
        'https': 'true',
        'type': '',
        'version': '2.28.5',
        'dpr': '1.25',
        'dev': '1',
        'cb': cb,
        'ipv6': 'false',
        'runEnv': '10',
        'group': '',
        'scene': '',
        'lang': 'zh-CN',
        'sdkVersion': '',
        'loadVersion': '2.5.4',
        'iv': '4',
        'user': '',
        'width': '300',
        'audio': 'false',
        'sizeType': '10',
        'smsVersion': 'v3',
        'token': '1840e95eb22b4145b812e94fb9c10cf6',
        'callback': '__JSONP_ha0pbzo_7',
    }
    response = requests.get('https://c.dun.163.com/api/v3/get', params=params, cookies=cookies, headers=headers)
    text=response.text
    print(text)
    data=json.loads(text[text.index('(')+1:text.rindex(')')])['data']
    bg=data['bg'][0]
    fg=data['front'][0]
    result={
        'cb': cb,
        'token': data['token'],
        'bg': bg if bg.startswith('http') else 'https:'+bg,
        'fg': fg if fg.startswith('http') else 'https:'+fg,
    }
    return result

def spider():
    print(get_cb())

def main():
    spider()

if __name__ == '__main__':
    main()
