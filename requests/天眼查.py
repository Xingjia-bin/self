import requests
from lxml import etree
import time
import sys
import random
import os

class TianYan:
    def __init__(self,company_id,fp,cookie,ip_proxies):
        self.fp = fp
        self.company_id = company_id
        self.ip_proxies = ip_proxies
        self.url = "https://www.tianyancha.com/company/{}".format(company_id)

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
        # 需要预先登录天眼查，打开源地址数据页面，将其中的Cookie复制到这里  (此Cookie的值需要保持登录状态，如果chrome中退出再登录，需要更新Cookie)
        self.cookie = cookie
        self.headers = {
            'User-Agent': random.choice(self.User_agents),
            'Cookie':self.cookie,
            'Referer':"https://www.tianyancha.com/login?from=https%3A%2F%2Fwww.tianyancha.com%2Fsearch%3Fkey%3D%25E9%2583%2591%25E5%25B7%259E%25E6%2583%25A0%25E5%25B7%259E%25E6%25B1%25BD%25E8%25BD%25A6%25E8%25BF%2590%25E8%25BE%2593%25E6%259C%2589%25E9%2599%2590%25E5%2585%25AC%25E5%258F%25B8",
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.tianyancha.com',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'Upgrade-Insecure-Requests': '1'
            }



    def get_html(self):
        response = requests.get(self.url,headers=self.headers,proxies=self.ip_proxies)  # whm
        res = response.content.decode()
        return res


    def get_start_crawl(self):  # 基本信息
        try:
            response = self.get_html()
        except Exception as e:
            print("公司{}网页读取失败，可能是ip或者登录的Cookie问题".format(self.company_id))
            raise Exception()
        if "快捷登录与短信登录" in response:
            print("爬取基本信息失败-需要登录 company_id:{}".format(self.company_id))
            # sys.exit(0)  # ※ 终止程序

        tree_html = etree.HTML(response)
        try:
            tr_list = tree_html.xpath('//*[@id="_container_baseInfo"]/table/tbody/tr')
            # company_name = tree_html.xpath("//div[@class='box -company-box ']/div[@class='content']/div[@class='header']/span/span/h1/text()")[0]  # 公司名
            company_name = tree_html.xpath("//div[@class='container company-header-block ']/div[3]/div[@class='content']/div[@class='header']/span/span/h1/text()")[0]  # 公司名  ※ 定位问题

            people_name = tr_list[0].xpath("td[2]//div[@class='humancompany']/div[@class='name']/a/text()")[0]  # 法定代表人
            company_status = tr_list[0].xpath("td[4]/text()")[0]  # 经营状态
            company_start_date = tr_list[1].xpath("td[2]/text()")[0]  # 成立日期
            company_zhuce = tr_list[2].xpath("td[2]/div/text()")[0]  # 注册资本
            company_shijiao = tr_list[3].xpath("td[2]/text()")[0]  # 实缴资本
            gongshanghao = tr_list[3].xpath("td[4]/text()")[0]  # 工商注册号
            xinyong_code = tr_list[4].xpath("td[2]/span/span/text()")[0]  # 统一信用代码
            nashuirenshibiehao = tr_list[4].xpath("td[4]/span/span/text()")[0]  # 纳税人识别号
            zhuzhijigou_code = tr_list[4].xpath("td[6]/span/span/text()")[0]  # 组织机构代码
            yingyeqixian = tr_list[5].xpath('td[2]/span/text()')[0].replace(' ', '')  # 营业期限
            people_zizi = tr_list[5].xpath('td[4]/text()')[0]  # 纳税人资质
            check_date = tr_list[5].xpath('td[6]/text()')[0]  # 核准日期
            leixing = tr_list[6].xpath('td[2]/text()')[0]  # 企业类型
            hangye = tr_list[6].xpath('td[4]/text()')[0]  # 行业
            people_number = tr_list[6].xpath('td[6]/text()')[0]  # 人员规模
            canbaorenshu = tr_list[7].xpath('td[2]/text()')[0]  # 参保人数
            dengjijiguan = tr_list[7].xpath('td[4]/text()')[0]  # 登记机关
            old_name = tr_list[8].xpath("td[2]//span[@class='copy-info-box']/span/text()")[0]  # 曾用名
            dizhi = tr_list[9].xpath('td[2]/span/span/span/text()')[0]  # 注册地址
            fanwei = tr_list[10].xpath('td[2]/span/text()')[0]  # 经营范围

            head_content = "法定代表人:{}\x01公司名:{}\x01经营状态:{}\x01成立日期:{}\x01注册资本:{}\x01实缴资本:{}\x01工商注册号:{}\x01统一信用代码:{}\x01纳税人识别号:{}\x01组织机构代码:{}" \
                           "\x01营业期限:{}\x01纳税人资质:{}\x01核准日期:{}\x01企业类型:{}\x01行业:{}\x01人员规模:{}\x01参保人数:{}\x01登记机关:{}\x01曾用名:{}\x01" \
                           "注册地址:{}\x01经营范围:{}".format(people_name,company_name,company_status,company_start_date,company_zhuce,company_shijiao,
                                                       gongshanghao,xinyong_code,nashuirenshibiehao,zhuzhijigou_code,yingyeqixian,people_zizi,check_date,
                                                       leixing,hangye,people_number,canbaorenshu,dengjijiguan,old_name,dizhi,fanwei)
            print(head_content,file=self.fp)
        except Exception as e:
            # print(self.response)
            print("公司{}的头部基本信息提取失败".format(self.company_id))
            # a = 1/0
            raise Exception()  # 手动引发异常，等同于a=1/0


    def kaiting(self):
        # 将公司ID替换掉就可以了
        company_id = self.company_id
        print("开庭公告",file=self.fp)
        for pg_num in range(1, 11):
            kt_ult = []
            # 分页修改announcementcourt和Cookie即可，每个字段的分页都有一个固定的Cookie,接下来查看这样是否会封IP  (本地电脑需要登录，而且Cookie就是登录后数据页面的Cookie)
            ss_url = 'https://www.tianyancha.com/pagination/announcementcourt.xhtml?TABLE_DIM_NAME=manageDangerous&ps=10&pn={}&id={}'.format(
                pg_num, company_id)
            ss_headers = {
                'User-Agent': random.choice(self.User_agents),
                'Cookie':self.cookie,
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'www.tianyancha.com',
                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            }
            # ss_page_status = requests.get(url=ss_url, headers=ss_headers).status_code

            # print(ss_page_status)
            response = requests.get(url=ss_url, headers=ss_headers,allow_redirects=False,proxies=self.ip_proxies).content.decode()
            if "抱歉，没有找到相关信息，请更换关键词重试" in response:
                break
            # print(response)
            tree_html = etree.HTML(response)
            kt_list = tree_html.xpath('//tbody/tr')
            if kt_list != '' and len(kt_list) > 0:
                for tr in kt_list:
                    try:
                        tds = tr.xpath("td")
                        court_order = tds[0].xpath("text()")[0]
                        court_date = tds[1].xpath("text()")[0]  # 开庭日期
                        court_num = tds[2].xpath("span/text()")[0]  # 案号
                        court_reason = tds[3].xpath("span/text()")[0]  # 案由
                        court_sta = tds[4].xpath("div")
                        court_sta_list = []
                        for i in court_sta:
                            court_sta_list.append(i.xpath("string(.)"))
                        court_status = " ".join(court_sta_list)  # 案件身份
                        court_law = tds[5].xpath("span/text()")[0]  # 审理法院
                        kt_ult.append("序号:{}\x01开庭日期:{}\x01案号:{}\x01案由:{}\x01案件身份:{}\x01审理法院:{}".format(court_order,court_date, court_num,
                                                                                               court_reason,
                                                                                               court_status, court_law))
                    except Exception as e:
                        print("公司{}此条开庭公告信息无法解析。第{}页".format(self.company_id,pg_num), e)
                        raise Exception("")
            else:
                break
            for elm in kt_ult:
                print(elm,file=self.fp)


    def lawsuitwhm(self):
        # 将公司ID替换掉就可以了
        company_id = self.company_id
        print("法律诉讼",file=self.fp)
        for pg_num in range(1, 11):  # 法律诉讼爬10个页面即可
            ss_ult = []
            # 法律诉讼的Cookie也需要登录后的数据页面中的Cookie
            ss_url = 'https://www.tianyancha.com/pagination/lawsuit.xhtml?TABLE_DIM_NAME=manageDangerous&ps=10&pn={}&id={}'.format(
                pg_num, company_id)
            ss_headers = {
                'User-Agent': random.choice(self.User_agents),
                'Cookie': self.cookie,
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'www.tianyancha.com',
                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            }
            # ss_page_status = requests.get(url=ss_url, headers=ss_headers).status_code

            # print(ss_page_status)
            response = requests.get(url=ss_url, headers=ss_headers,allow_redirects=False,proxies=self.ip_proxies).content.decode()

            if "抱歉，没有找到相关信息，请更换关键词重试" in response:
                break
            ss_tree = etree.HTML(response)
            ss_list = ss_tree.xpath('//tbody/tr')
            if len(ss_list) != 0:
                for tr in ss_list:
                    try:
                        tds = tr.xpath("td")
                        lawsuit_order = tds[0].xpath("text()")[0]
                        lawsuit_name = tds[1].xpath("text()")[0]  # 案件名称
                        lawsuit_reason = tds[2].xpath("span/text()")[0]  # 案由
                        lawsuit_sta = tds[3].xpath("div/div/div/span")  # 在本案中身份
                        lawsuit_sta_list = []
                        for i in lawsuit_sta:
                            lawsuit_sta_list.append(i.xpath("string(.)"))
                        lawsuit_status = "".join(lawsuit_sta_list)  # 在本案中身份
                        lawsuit_result = tds[4].xpath("div/div/text()")[0]  # 裁判结果
                        lawsuit_result = lawsuit_result.replace('\n', '').replace(' ','').replace('\r', '')
                        lawsuit_money = tds[5].xpath("span/text()")[0]  # 案件金额
                        ss_ult.append("序号:{}\x01案件名称:{}\x01案由:{}\x01在本案中身份:{}\x01裁判结果:{}\x01案件金额:{}".format(lawsuit_order,lawsuit_name,lawsuit_reason,lawsuit_status,lawsuit_result,lawsuit_money))
                    except Exception as e:
                        print("公司{}此条法律诉讼信息未能解析。第{}页".format(self.company_id,pg_num),e)
                        raise Exception("")
            else:
                break
            for one_ult in ss_ult:
                print(one_ult,file=self.fp)


    def fayuangonggao(self):
        # 法院公告解析：
        print("法院公告",file=self.fp)
        company_id = self.company_id
        for pg_num in range(1,11):
            url = 'https://www.tianyancha.com/pagination/court.xhtml?TABLE_DIM_NAME=manageDangerous&ps=10&pn={}&id={}'.format(
                pg_num, company_id)

            headers = {
                'User-Agent': random.choice(self.User_agents),  # 下面的Cookie需要换上本电脑上数据页面的Cookie
                'Cookie': self.cookie,
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'www.tianyancha.com',
                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            }
            response = requests.get(url=url, headers=headers,allow_redirects=False,proxies=self.ip_proxies).content.decode()
            if "抱歉，没有找到相关信息，请更换关键词重试" in response:
                break
            # print(response)
            gonggao_ult = []
            gonggao_tree = etree.HTML(response)
            gonggao_list = gonggao_tree.xpath('//tbody/tr')
            if len(gonggao_list) != 0:
                for tr in gonggao_list:
                    try:
                        tds = tr.xpath("td")
                        gg_order = tds[0].xpath("text()")[0]
                        gg_date = tds[1].xpath("text()")[0]  # 刊登日期
                        gg_num = tds[2].xpath("text()")[0]  # 案号
                        gg_reason = tds[3].xpath("text()")[0]  # 案由
                        e = tds[4].xpath("div")
                        estr = []
                        for i in e:
                            estr.append(i.xpath("string(.)"))
                        gg_status = "\x01".join(estr)  # 案件身份
                        gg_type = tds[5].xpath("text()")[0]  # 公告类型
                        gg_law = tds[6].xpath("text()")[0]  # 法院

                        gonggao_ult.append("序号:{}\x01刊登日期:{}\x01案号:{}\x01案由:{}\x01案件身份:{}\x01公告类型:{}\x01法院:{}".format(gg_order,gg_date,gg_num,gg_reason,gg_status,gg_type,gg_law))
                    except Exception as e:
                        print("公司{}此条法院公告信息无法解析。第{}页".format(self.company_id,pg_num),e)
                        raise Exception("")
            else:
                break
            for elm in gonggao_ult:
                print(elm,file=self.fp)

    def beizhixing(self):
        print("被执行人",file=self.fp)

        company_id = self.company_id
        for pg_num in range(1,11):
            zhixingren_ult = []
            url = 'https://www.tianyancha.com/pagination/zhixing.xhtml?TABLE_DIM_NAME=manageDangerous&ps=10&pn={}&id={}'.format(
                pg_num, company_id)

            headers = {
                'User-Agent': random.choice(self.User_agents),  # 下面的Cookie需要换上本电脑上数据页面的Cookie
                'Cookie': self.cookie,
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'www.tianyancha.com',
                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            }
            response = requests.get(url=url, headers=headers, allow_redirects=False,proxies=self.ip_proxies).content.decode()
            if "抱歉，没有找到相关信息，请更换关键词重试" in response:
                break
            # print(response)
            zhixingren_tree = etree.HTML(response)
            try:
                zhixingren_list = zhixingren_tree.xpath('//tbody/tr')
            except Exception as e:
                break
            if len(zhixingren_list) != 0:
                for tr in zhixingren_list:
                    try:
                        tds = tr.xpath("td")
                        zhixing_order = tds[0].xpath("text()")[0]  # 序号
                        zhixing_date = tds[1].xpath("text()")[0]  # 立案日期
                        zhixing_num = tds[2].xpath("text()")[0]  # 案号
                        zhixing_money = tds[3].xpath("text()")[0]  # 执行标的
                        zhixing_lawer = tds[4].xpath("text()")[0]  # 执行法院

                        zhixingren_ult.append("序号:{}\x01立案日期:{}\x01案号:{}\x01执行标的:{}\x01执行法院:{}".format(zhixing_order,zhixing_date,zhixing_num,zhixing_money,zhixing_lawer))
                    except Exception as e:
                        print("公司{}此条法院公告信息无法解析。第{}页".format(self.company_id,pg_num),e)
                        raise Exception("")
            else:
                break
            for elm in zhixingren_ult:
                print(elm,file=self.fp)

    def lian_message(self):
        print("立案信息",file=self.fp)
        company_id = self.company_id
        for pg_num in range(1,11):
            url = 'https://www.tianyancha.com/pagination/courtRegister.xhtml?TABLE_DIM_NAME=manageDangerous&ps=10&pn={}&id={}'.format(
                pg_num, company_id)
            headers = {
                'User-Agent': random.choice(self.User_agents),  # 下面的Cookie需要换上本电脑上数据页面的Cookie
                'Cookie': self.cookie,
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'www.tianyancha.com',
                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            }
            response = requests.get(url=url, headers=headers, allow_redirects=False,proxies=self.ip_proxies).content.decode()
            if "抱歉，没有找到相关信息，请更换关键词重试" in response:
                break
            # print(response)
            lian_ult = []
            lian_tree = etree.HTML(response)
            try:
                lian_list = lian_tree.xpath('//tbody/tr')
            except Exception as e:
                break
            if len(lian_list) != 0:
                for tr in lian_list:
                    try:
                        tds = tr.xpath("td")
                        register_order = tds[0].xpath("text()")[0]  # 序号
                        register_date = tds[1].xpath("text()")[0]  # 立案日期
                        register_num = tds[2].xpath("text()")[0]  # 案号
                        register_sta = tds[3].xpath("div")
                        register_status = []
                        for i in register_sta:
                            register_status.append(i.xpath("string(.)"))
                        register_status = "\x01".join(register_status)  # 案件身份
                        register_law = tds[4].xpath("text()")[0]  # 法院
                        lian_ult.append(
                            "序号:{}\x01立案日期:{}\x01案号:{}\x01案件身份:{}\x01法院:{}".format(register_order,register_date, register_num, register_status,
                                                                          register_law))
                    except Exception as e:
                        print("公司{}此条立案信息无法解析。第{}页".format(self.company_id,pg_num), e)
                        raise Exception("")
            else:
                break
            for elm in lian_ult:
                print(elm,file=self.fp)

    def xingzheng(self):
        print("行政处罚",file=self.fp)
        company_id = self.company_id
        for pg_num in range(1,11):
            url = 'https://www.tianyancha.com/pagination/mergePunishCount.xhtml?TABLE_DIM_NAME=manageDangerous&ps=10&pn={}&id={}'.format(
                pg_num, company_id)
            headers = {
                'User-Agent': random.choice(self.User_agents),  # 下面的Cookie需要换上本电脑上数据页面的Cookie
                'Cookie': self.cookie,
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'www.tianyancha.com',
                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            }
            response = requests.get(url=url, headers=headers, allow_redirects=False,proxies=self.ip_proxies).content.decode()
            if "抱歉，没有找到相关信息，请更换关键词重试" in response:
                break
            # print(response)
            xingzheng_ult = []
            xingzheng_tree = etree.HTML(response)
            try:
                xingzheng_list = xingzheng_tree.xpath('//tbody/tr')
            except Exception as e:
                break
            if len(xingzheng_list) != 0:
                for tr in xingzheng_list:
                    try:
                        tds = tr.xpath("td")
                        penalty_order = tds[0].xpath("text()")[0]  # 序号
                        penalty_date = tds[1].xpath("text()")[0]  # 处罚日期
                        penalty_books = tds[2].xpath("div/text()")[0]  # 决定文书号
                        penalty_reason = tds[3].xpath("div/div/text()")[0]  # 处罚事由
                        penalty_result = tds[4].xpath("div/div/text()")[0]  # 处罚结果
                        penalty_unit = tds[5].xpath("text()")[0]  # 处罚单位
                        penalty_source = tds[6].xpath("span/text()")[0]  # 数据来源

                        # print(penalty_date,penalty_books,penalty_reason,penalty_result,penalty_unit,penalty_source)
                        xingzheng_ult.append(
                            "序号:{}\x01处罚日期:{}\x01决定文书号:{}\x01处罚事由:{}\x01处罚结果:{}\x01处罚单位:{}\x01数据来源:{}".format(
                                penalty_order,penalty_date,penalty_books,penalty_reason,penalty_result,penalty_unit,penalty_source))
                    except Exception as e:
                        print("公司{}此条行政处罚无法解析。第{}页".format(self.company_id,pg_num), e)
                        raise Exception("")
            else:
                break
            for elm in xingzheng_ult:
                print(elm,file=self.fp)

    def body_run(self):
        self.get_start_crawl()  # 基本信息
        self.kaiting()  # 开庭公告
        self.lawsuitwhm()  # 法律诉讼
        self.fayuangonggao()  # 法院公告
        self.beizhixing()  # 被执行人
        self.lian_message()  # 立案信息
        self.xingzheng()  # 行政处罚


