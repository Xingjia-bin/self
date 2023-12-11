import requests
from bs4 import BeautifulSoup

# 获取视频的 cid
def get_cid(aid):
    url = f'https://api.bilibili.com/x/player/pagelist?aid={aid}&jsonp=jsonp'
    res = requests.get(url)
    data = res.json()
    return data['data'][0]['cid']

# 获取弹幕
def get_danmu(cid):
    url = f'http://comment.bilibili.com/{cid}.xml'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    danmu_list = soup.find_all('d')
    for danmu in danmu_list:
        print(danmu.text)

def get_danmu(cid):
    url = f'http://comment.bilibili.com/{cid}.xml'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    danmu_list = soup.find_all('d')
    with open('danmu.txt', 'w', encoding='utf-8') as f:
        for danmu in danmu_list:
            # 获取弹幕文本
            text = danmu.text
            # 获取弹幕属性
            p = danmu['p'].split(',')
            # 获取发送时间（以视频开始时间为基准）
            send_time = float(p[0])
            f.write(f'弹幕：{text}，发送时间：{send_time}\n')

if __name__ == '__main__':
    aid = input('请输入视频 aid：')
    cid = get_cid(aid)