import requests

class Spider:

    def __init__(self, url):
        # 初始化 Spider 类的实例
        # 参数 url：要爬取的网页的基础 URL
        self.__uid = ''  # 用于存储爬虫实例的私有属性
        self.__real_base_url = ''  # 用于存储实际的基础 URL 的私有属性
        self.__base_url = url  # 存储用户提供的基础 URL 的私有属性
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }  # 存储请求头的私有属性，模拟浏览器请求
        self.session = requests.Session()  # 创建一个会话对象，用于跨多个请求保持会话状态

    def __set_real_url(self):
        # 私有方法，用于获取实际的基础 URL
        request = self.session.get(self.__base_url, headers=self.__headers)  # 发送 GET 请求获取网页内容
        real_url = request.url  # 获取请求的实际 URL
        self.__real_base_url = real_url[:len(real_url) - len('default2.aspx')]  # 剔除默认的后缀部分，得到实际的基础 URL
        return request  # 返回请求对象
    
    def get_cookie():

        request = requests.get('http://59.61.86.138:18080') 

        cookie = requests.cookie

        return cookie
