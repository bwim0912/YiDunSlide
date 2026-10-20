import json
import execjs

from 易盾get接口 import get_cb
from 计算距离 import get_distance


def get_check_params(token, slide):
    """token 来自 易盾get接口.get_cb()，slide 来自 计算距离.get_distance()。

    slide 必须是 300 宽度基准的像素（JS 里要算 slide/300*100），
    所以调用 get_distance 时要传 display_width=300。
    """
    src = open('易盾check接口.js', mode='r', encoding='utf-8').read()
    return json.loads(execjs.compile(src).call('get_check_params', token, slide))


def get_cb_value():
    """单独调一次 JS 的 get_cb()：check 请求用的是新算的 cb，和 get 那次不同。"""
    src = open('get_cb.js', mode='r', encoding='utf-8').read()
    return execjs.compile(src).call('get_cb')


def get_callback():
    """check 的 JSONP callback 名，由 JS 里的 get_callback() 生成。"""
    src = open('易盾check接口.js', mode='r', encoding='utf-8').read()
    return execjs.compile(src).call('get_callback')


def run():
    info = get_cb()                                 # 一次 get：token + 两张图
    token = info['token']
    slide = get_distance(info, display_width=300)   # 同一张图算位移，换算到 300 基准
    params = get_check_params(token, slide)         # d / m / p / f / ext
    print('token :', token)
    print('slide :', slide)
    print('params:', params)
    return token, slide, params


if __name__ == '__main__':
    run()
