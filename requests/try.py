import requests
from lxml import etree
import time
import sys
import random
import os
import re
# from .Tianyan_head import get_company_head
# from .Tianyan_body import TianYan
# from z1217.Tianyan_body import TianYan
# from .Tianyan_body import TianYan
from 天眼查 import TianYan

class CompanySetting:
    def __init__(self,var):
        self.User_agents = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        ]
        # 需要预先登录天眼查，打开源地址数据页面，将其中的Cookie复制到这里  (此Cookie的值需要保持登录状态，如果chrome中退出再登录，需要更新Cookie)-↓
        # 需要更换Cookie,过老的Cookie也会无效，需要点击图片验证
        # 更改代理IP
        # self.cookie = "TYCID=970a0360595911ecb844678fcc48c6b4; ssuid=7782420900; _ga=GA1.2.205529974.1639100190; creditGuide=1; tyc-user-phone=%255B%252215838072824%2522%255D; _bl_uid=51kg7wILzwmt33jnnh8b8gq4g88m; aliyungf_tc=975133a0586b9d8247910635fab0120f2dfb47303db68899981b96efb22ecb7a; csrfToken=GPfdbeBsdJFMKJ9PS4OZyF-k; bannerFlag=true; jsid=https%3A%2F%2Fwww.tianyancha.com%2F%3Fjsid%3DSEM-BAIDU-PZ-SY-2021112-JRGW; relatedHumanSearchGraphId=529120041; relatedHumanSearchGraphId.sig=1e6-htbuJ3oK-8m0maPt0n-jiP2_2MK-xlrwLZW5Oy0; bdHomeCount=6; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1639638751,1639638959,1639642785,1639645038; searchSessionId=1639645046.08106995; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215838072824%22%2C%22first_id%22%3A%2217da1fc06a69ec-07c085ac54da9c-978183a-1327104-17da1fc06a7954%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217da1fc06a69ec-07c085ac54da9c-978183a-1327104-17da1fc06a7954%22%7D; tyc-user-info-save-time=1639704027297; tyc-user-info={%22mobile%22:%2215838072824%22%2C%22state%22:%220%22%2C%22vipManager%22:%220%22}; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTgzODA3MjgyNCIsImlhdCI6MTYzOTcwNDAyNiwiZXhwIjoxNjcxMjQwMDI2fQ._LllvS1X_MSI7IDLrBIvG1wIKvjVtALqFR81Ixmhke5msBxTizzR4mXFXuQaTyvUybvgRX31_FlK6P6qzCkoRA; acw_tc=2f6fc11d16397075828226503ec3489a686979b226b0b3504fa789a6ffd041; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1639707587; CT_TYCID=0d4dc14181ed451994ed050a41c2e73c; cloud_token=00d53042f06548f6b7d16614a061db98; cloud_utm=6aa5eb580a1c4ff9bf91e3172576f909"
        # self.cookie = "TYCID=970a0360595911ecb844678fcc48c6b4; ssuid=7782420900; _ga=GA1.2.205529974.1639100190; creditGuide=1; tyc-user-phone=%255B%252215838072824%2522%255D; _bl_uid=51kg7wILzwmt33jnnh8b8gq4g88m; aliyungf_tc=975133a0586b9d8247910635fab0120f2dfb47303db68899981b96efb22ecb7a; csrfToken=GPfdbeBsdJFMKJ9PS4OZyF-k; bannerFlag=true; jsid=https%3A%2F%2Fwww.tianyancha.com%2F%3Fjsid%3DSEM-BAIDU-PZ-SY-2021112-JRGW; relatedHumanSearchGraphId=529120041; relatedHumanSearchGraphId.sig=1e6-htbuJ3oK-8m0maPt0n-jiP2_2MK-xlrwLZW5Oy0; bdHomeCount=6; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1639638751,1639638959,1639642785,1639645038; searchSessionId=1639645046.08106995; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215838072824%22%2C%22first_id%22%3A%2217da1fc06a69ec-07c085ac54da9c-978183a-1327104-17da1fc06a7954%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217da1fc06a69ec-07c085ac54da9c-978183a-1327104-17da1fc06a7954%22%7D; tyc-user-info-save-time=1639704027297; tyc-user-info={%22mobile%22:%2215838072824%22%2C%22state%22:%220%22%2C%22vipManager%22:%220%22}; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTgzODA3MjgyNCIsImlhdCI6MTYzOTcwNDAyNiwiZXhwIjoxNjcxMjQwMDI2fQ._LllvS1X_MSI7IDLrBIvG1wIKvjVtALqFR81Ixmhke5msBxTizzR4mXFXuQaTyvUybvgRX31_FlK6P6qzCkoRA; CT_TYCID=0d4dc14181ed451994ed050a41c2e73c; RTYCID=b5ba30f9d70e40c18d80b48fe303f22b; bannerHide=15838072824; acw_tc=781bad4616397361274246135e1eb3f8b23bff47f6f268b363aabff7f4ceca; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1639736175; cloud_token=7137d132ab654409a8a891f46f295ab1; cloud_utm=62da596d28c9401bac8a3c504346eaba"
        # self.cookie = "TYCID=970a0360595911ecb844678fcc48c6b4; ssuid=7782420900; _ga=GA1.2.205529974.1639100190; creditGuide=1; tyc-user-phone=%255B%252215838072824%2522%255D; _bl_uid=51kg7wILzwmt33jnnh8b8gq4g88m; aliyungf_tc=975133a0586b9d8247910635fab0120f2dfb47303db68899981b96efb22ecb7a; csrfToken=GPfdbeBsdJFMKJ9PS4OZyF-k; bannerFlag=true; jsid=https%3A%2F%2Fwww.tianyancha.com%2F%3Fjsid%3DSEM-BAIDU-PZ-SY-2021112-JRGW; relatedHumanSearchGraphId=529120041; relatedHumanSearchGraphId.sig=1e6-htbuJ3oK-8m0maPt0n-jiP2_2MK-xlrwLZW5Oy0; bdHomeCount=6; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1639638751,1639638959,1639642785,1639645038; searchSessionId=1639645046.08106995; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215838072824%22%2C%22first_id%22%3A%2217da1fc06a69ec-07c085ac54da9c-978183a-1327104-17da1fc06a7954%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217da1fc06a69ec-07c085ac54da9c-978183a-1327104-17da1fc06a7954%22%7D; CT_TYCID=0d4dc14181ed451994ed050a41c2e73c; RTYCID=b5ba30f9d70e40c18d80b48fe303f22b; acw_tc=781bad4a16398202951244078e10561a742e1265ed4753147617e30ed7430a; cloud_token=2eed115dc8734abf9d2a27258fa072cf; cloud_utm=b8e11d75c9a5473c95358dd5beff997d; tyc-user-info={%22mobile%22:%2215838072824%22%2C%22state%22:%220%22%2C%22vipManager%22:%220%22}; tyc-user-info-save-time=1639820536903; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTgzODA3MjgyNCIsImlhdCI6MTYzOTgyMDUzNywiZXhwIjoxNjcxMzU2NTM3fQ.IQexhM-41JQUHWDQMV8MZR388CqFT-U0u24q_O4Xjx45-vdU8wFH1zuGrxyPAey7DkbWUuM9WU2fUZKG2bJt8A; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1639820539"
        # self.cookie = "aliyungf_tc=282ebba707a03b502b075b0cdd1393a6f2720a797a955a717160cc4bbdb89fbc; csrfToken=WuVruO4GsAFIc9z5DdQxtlAR; TYCID=a8a5bdd05db911ec8061e5e64f8765b8; ssuid=4585560966; bannerFlag=true; creditGuide=1; _ga=GA1.2.1523420552.1639581264; tyc-user-phone=%255B%252215838072824%2522%255D; jsid=https%3A%2F%2Fwww.tianyancha.com%2F%3Fjsid%3DSEM-BAIDU-PZ-SY-2021112-JRGW; searchSessionId=1639670771.66783963; relatedHumanSearchGraphId=3149325530; relatedHumanSearchGraphId.sig=HJivDEDhp8niuTtrieCF_t56fZHwONjuSprSp-AkZ88; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215838072824%22%2C%22first_id%22%3A%2217dbea89958208-0911ada0d7e41f-978183a-1382400-17dbea89959ced%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E5%A4%A9%E7%9C%BC%E6%9F%A5%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%7D%2C%22%24device_id%22%3A%2217dbea89958208-0911ada0d7e41f-978183a-1382400-17dbea89959ced%22%7D; _gid=GA1.2.849271308.1639890728; _bl_uid=1sknjxCmczFsFIom9l9jr1w8w0Xk; tyc-user-info={%22mobile%22:%2215838072824%22%2C%22state%22:%220%22%2C%22vipManager%22:%220%22}; tyc-user-info-save-time=1639891233305; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTgzODA3MjgyNCIsImlhdCI6MTYzOTg5MTIzMiwiZXhwIjoxNjcxNDI3MjMyfQ.hla9H3LbFzE3-2IDDW4Xw_PosxVHzK0ATnZQUSffRQyWWQx95stFK8QuQA-UaJhV8VqSJGwojvnilxGUPilrLA; RTYCID=3888f8318b3e437c8327a699fa3a611f; CT_TYCID=1c090123cbab4efd8d0462dd297a2be2; bdHomeCount=1; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1639581261,1639890723,1639894039; acw_tc=707c9f7416398943324086228e5c82b88b3612a564754bc05f7710f8edac8d; acw_sc__v2=61becd3c362220c666fbe902c836b81079267abd; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1639894507; cloud_token=aeb2c3ff7c344c0e9e448e3fc68643df; cloud_utm=2cd2f64ef4d0433684d8901b1d22c97e"
        # 这是需要修改的地方
        self.cookie = "aliyungf_tc=282ebba707a03b502b075b0cdd1393a6f2720a797a955a717160cc4bbdb89fbc; csrfToken=WuVruO4GsAFIc9z5DdQxtlAR; TYCID=a8a5bdd05db911ec8061e5e64f8765b8; ssuid=4585560966; bannerFlag=true; creditGuide=1; _ga=GA1.2.1523420552.1639581264; tyc-user-phone=%255B%252215838072824%2522%255D; jsid=https%3A%2F%2Fwww.tianyancha.com%2F%3Fjsid%3DSEM-BAIDU-PZ-SY-2021112-JRGW; searchSessionId=1639670771.66783963; relatedHumanSearchGraphId=3149325530; relatedHumanSearchGraphId.sig=HJivDEDhp8niuTtrieCF_t56fZHwONjuSprSp-AkZ88; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215838072824%22%2C%22first_id%22%3A%2217dbea89958208-0911ada0d7e41f-978183a-1382400-17dbea89959ced%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E5%A4%A9%E7%9C%BC%E6%9F%A5%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%7D%2C%22%24device_id%22%3A%2217dbea89958208-0911ada0d7e41f-978183a-1382400-17dbea89959ced%22%7D; _gid=GA1.2.849271308.1639890728; _bl_uid=1sknjxCmczFsFIom9l9jr1w8w0Xk; RTYCID=3888f8318b3e437c8327a699fa3a611f; CT_TYCID=1c090123cbab4efd8d0462dd297a2be2; bdHomeCount=1; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1639581261,1639890723,1639894039; cloud_token=9c9711e8bdb6475cb7f6819d3cba55d8; acw_tc=707c9f6816398972133788598e76c87b9cc060eace0ffcccede3e98136ec98; acw_sc__v2=61bed87db3318ccfc4dc7a6bc493a83ddf8162f0; tyc-user-info={%22mobile%22:%2215838072824%22%2C%22state%22:%220%22%2C%22vipManager%22:%220%22}; tyc-user-info-save-time=1639897221599; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTgzODA3MjgyNCIsImlhdCI6MTYzOTg5NzIyMCwiZXhwIjoxNjcxNDMzMjIwfQ.L5BmUloturqBaXRmetCI_szFbDikF6vXn8EPT-G8F8YeblfdTY6LD7yduZPYDY8QSBeQDRROLVutwO1UxCZfcw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1639897223"
        # 这也是需要修改的地方
        self.ip = "223.247.87.198:34039"

        ip_host = self.ip.split(":")[0]
        ip_port = self.ip.split(":")[1]
        # 非账号密码验证
        proxyMeta = "http://{}:{}".format(ip_host, ip_port)
        self.ip_proxies = {
            "http": proxyMeta,
            "https": proxyMeta
        }

        self.headers = {
            'User-Agent': random.choice(self.User_agents),
            'Cookie': self.cookie,
            'Referer': "https://www.tianyancha.com/login?from=https%3A%2F%2Fwww.tianyancha.com%2Fsearch%3Fkey%3D%25E9%2583%2591%25E5%25B7%259E%25E6%2583%25A0%25E5%25B7%259E%25E6%25B1%25BD%25E8%25BD%25A6%25E8%25BF%2590%25E8%25BE%2593%25E6%259C%2589%25E9%2599%2590%25E5%2585%25AC%25E5%258F%25B8",
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.tianyancha.com',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'Upgrade-Insecure-Requests': '1'
        }
        self.var = var.strip()

    def is_number(self,x):
        try:
            x = int(x)
            return isinstance(x, int)
        except ValueError:
            return False


    def get_id_or_name(self):
        var = self.var
        # if self.is_number(var):  # 如果是公司ID的话
        #     url = "https://www.tianyancha.com/company/{}".format(var)
        #     response = requests.get(url, headers=self.headers)
        #     response = response.content.decode()
        #     if "快捷登录与短信登录" in response:
        #         print("需要登录 company_name:{}".format(var))
        #         sys.exit(0)  # ※ 终止程序
        #     etree_html = etree.HTML(response)
        #     try:
        #         # 求公司名
        #         h1 = etree_html.xpath('//div[@class="container company-header-block "]/div[3]/div[@class="content"]/div[@class="header"]/span/span/h1/text()')[0]
        #         # print(var,h1)
        #         return var,h1  # 公司Id和公司名
        #     except Exception as e:
        #         # print("公司:{}读取错误".format(var))
        #         return None,None
        if self.is_number(var):  # 如果是公司ID的话
            return var,None
        else:  # 如果是公司名
            url = "https://www.tianyancha.com/search?key={}".format(var)
            try:
                response = requests.get(url,headers=self.headers,proxies=self.ip_proxies).content.decode()  # 加上代理IP
            except Exception as e:
                print("该换ip了")
                sys.exit(0)
            if "快捷登录与短信登录" in response:
                print("需要登录 company_name:{}".format(var))
                sys.exit(0)  # ※ 终止程序
            etree_html = etree.HTML(response)
            try:
                div_s = etree_html.xpath("//div[@class='result-list sv-search-container']/div[1]")
                # print(len(div_s))  # 如果长度为0，则需要登录,而上面的Cookie和Referer和User-Agent已经有了登录信息，说明该号已被禁爬
                # print(self.response)  # 如果没有”登录“字眼就行
                # print(len(div_s))
                if len(div_s) > 0:  # 只拿取第一个公司的数据
                    contents = div_s[0].xpath("div/div[@class='content']/div[@class='header']/a/@sensors-event-ch")[0]
                    ret_id = re.findall("&card_id=(.*?)&item=", contents)[0]
                    ret_name = re.findall("&card_name=(.*?)&card_type", contents)[0]
                    # print(ret_id, ret_name)
                    return ret_id,ret_name
                else:
                    print("无法访问-通过公司名爬ID，需要更新登录Cookie或没有该公司信息")
                    # print(self.response)
                    return None,None
            except Exception as e:
                # print("公司:{}读取错误".format(var))
                return None, None



if __name__ == '__main__':
    start_time = time.time()  # 开始时间
    # with open("zSD_company_id.txt","r",encoding="utf-8") as f:
    #     content = f.readlines()
    # var_list = [car_id.strip() for car_id in content]
    # company_list = list(set(var_list))
    # company_list.sort(key=var_list.index)  # 去重排序不改变元素相对位置
    # company_list中可以写公司ID，也可以直接写公司名
    company_list = ["844565574", "2319114574", "2317302446", "789235759", "2964355333","山东广鑫宇汽车运输有限公司","山东宇汽车运输有限公司","河南国宾汽车运输有限公司","3273353756"]
    print(len(company_list),company_list)
    company_index = 0

    for var in company_list:
        company_index += 1  # 计数

        start2_time = time.time()
        Cs = CompanySetting(var)
        c_id,c_name = Cs.get_id_or_name()  # 拿到公司ID和公司名
        if c_id != None or c_name != None:
            if os.path.isfile("TY_{}.txt".format(c_id)):
                if int(os.path.getsize("TY_{}.txt".format(c_id))) == 0:  # 如果是空，删除
                    os.remove("TY_{}.txt".format(c_id))
            if os.path.isfile("TY_{}.txt".format(c_id)):  # 如果该公司信息已经爬取
                print("TY_{}.txt  pass".format(c_id))
            else:
                path = "TY_{}.txt".format(c_id)
                file_txt = open(path, "w")  # 新建一个文件(清空源文件内容)
                fp = open(path, 'a+', encoding='utf-8')
                try:
                    company_body_ty = TianYan(c_id,fp,Cs.cookie,Cs.ip_proxies)
                    company_body_ty.body_run()  # True or False
                    print("{} successful!  it cost time:{}".format(c_id,time.time()-start2_time))
                except Exception as e:  # 如果本条公司的数据爬取错误，则删除这个未爬完的txt
                    print("公司{}部分信息读取失败".format(c_id))
                    fp.close()
                    f_clear = open("TY_{}.txt".format(c_id), "w")  # 将爬取失败的文件清空 为0 k
                    # if os.path.isfile("TY_{}.txt".format(c_id)):
                    #     os.remove("TY_{}.txt".format(c_id))
                    # 发邮件记录
                    print("第{}个公司出现错误-files cost time:{}".format(company_index, time.time() - start_time))

                finally:
                    fp.close()  # 关闭文件 ※  需要及时关闭文件，不然程序循环再读取的时候如果该文件不关闭，那么文件大小就是0，而且程序报错显示该文件被其他进程占用
        else:
            print("这个公司{}的公司名字信息读取失败".format(var))
            # 发邮件记录
        time.sleep(random.random()*3)  # 随机间隔3秒以内
    print("{}-files cost time:{}".format(len(company_list),time.time()-start_time))


