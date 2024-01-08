import requests

class Spider:

    def __init__(self, url):
        # 初始化 Spider 类的实例
        # 参数 url：要爬取的网页的基础 URL
        self.__uid = ''  # 用于存储爬虫实例的私有属性
        self.__real_base_url = ''  # 用于存储实际的基础 URL 的私有属性
        self.__base_url = url  # 存储用户提供的基础 URL 的私有属性
        self.__headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '161',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': '59.61.86.138:18080',
            'Origin': 'http://59.61.86.138:18080',
            'Pragma': 'no-cache',
            'Referer': 'http://59.61.86.138:18080/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }  # 存储请求头的私有属性，模拟浏览器请求
        self.session = requests.Session()  # 创建一个会话对象，用于跨多个请求保持会话状态

    def save_cookie(self, response):
        # 保存从响应中获取的Cookie到会话中
        cookies = response.cookies
        self.session.cookies.update(cookies)

    def send_request(self):
        # 发送 GET 请求
        response = self.session.get(self.__base_url, headers=self.__headers)
        self.save_cookie(response)  # 保存Cookie到会话中
        return response  # 返回响应对象


