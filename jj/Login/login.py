# 导入驱动
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class Login_open():
    # 浏览器的获取
    driver = webdriver.Chrome()
    # 打开网址
    url = "http://192.168.1.42/user/login"
    driver.get(url)
    # 设置浏览器的最大窗口
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_id('username').send_keys('001549')
    driver.find_element_by_id("password").send_keys('123456')
    driver.find_element_by_xpath("//*[@id='formLogin']/div/div[3]/div/div/span/button").click()
    time.sleep(5)

# 业务质量管理模块 -打开
# driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/div").click()
# time.sleep(2)

# # 业务服务列表页 -打开
# driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[1]/a").click()
# time.sleep(2)
# # 服务质量总表 --打开
# driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[2]/a").click()
# time.sleep(2)
# # 申诉处理
# driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[3]/a").click()
# time.sleep(2)
# # 申诉结果
# driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[4]/a").click()
# time.sleep(2)
