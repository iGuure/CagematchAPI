# coding=utf-8
import scrapy
from scrapy.selector import Selector

class SimpleLoginSpider(scrapy.Spider):
	name = 'simplelogin'
	allowed_domains = ['pyw.cn']

	login_url = 'http://pyw.cn/user/login'

	login_check_url = 'http://pyw.cn/user/loginCheck'

	start_url = 'http://pyw.cn/order/userorders'

	# 需要提交的表单
	form_data = {
		'phoneNum1': '15820577524',
		'password': '12345678',
		'authCode1': ''
	}

	# start_requests是爬虫执行的第一个方法，故重写之
	# 请求GET login_url
	# 保存收到的cookie
	def start_requests(self):
		return [scrapy.Request(
			url = self.login_url,
			meta = {'cookiejar': 1},
			callback = self.post_login)]

	# 使用FormRequest.from_response，提交表单
	# 请求POST login_check_url
	# 使用刚才保存的cookie
	def post_login(self, response):
		return [scrapy.FormRequest.from_response(
			response,
			url = self.login_check_url,
			meta = {'cookiejar': response.meta['cookiejar']},
			formdata = self.form_data,
			callback = self.after_login,
			method = 'POST')]

	# 登陆成功后，开始请求其他页面
	# 请求GET start_url
	# 使用刚才保存的cookie
	def after_login(self, response):
		return [scrapy.Request(
			url = self.start_url,
			meta = {'cookiejar': response.meta['cookiejar']},
			callback = self.parse_details)]

	# 如果span[@class="order_title"]存在，那么模拟登陆成功！
	# 可以在此对response进行分析，爬取数据
	def parse_details(self, response):
		print(response.xpath('//span[@class="order_title"]').extract())