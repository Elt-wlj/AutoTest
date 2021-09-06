# 导入驱动
from selenium import webdriver
import time

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
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/div").click()
time.sleep(2)
# 业务服务列表页 -打开
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[1]/a").click()
time.sleep(2)
# 服务质量总表 --打开
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[2]/a").click()
time.sleep(2)
# 申诉处理
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[3]/a").click()
time.sleep(2)
# 申诉结果
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[4]/a").click()
time.sleep(2)
# 评估质量审核页面
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[5]/a").click()
time.sleep(2)
# 输入员工的姓名
driver.find_element_by_xpath(
    "//div[@class='table-page-search-wrapper']/form/div/div[1]/div/div[2]/div/span/input").send_keys('金文莉')
time.sleep(2)
# 输入员工的工号
driver.find_element_by_xpath(
    "//div[@class='table-page-search-wrapper']/form/div/div[2]/div/div[2]/div/span/input").send_keys('007480')
time.sleep(2)
# 日期的选择
driver.find_element_by_xpath("//span[@class='ant-calendar-picker']").click()
# 1、jquery移除属性 ----设置readonly为false属性  开始时间
js_start = "$('input:eq(3)').attr('readnoly',false)"
driver.execute_script(js_start)
input_datetime = driver.find_element_by_xpath("//div[@class='ant-calendar-date-panel']/div[1]/div[1]/div/input")
input_datetime.send_keys("2021-08-06")
time.sleep(2)

# 2、结束时间------
js_end = "$('input:eq(4)').attr('readnoly',false)"
driver.execute_script(js_end)
input_datetime = driver.find_element_by_xpath("//div[@class='ant-calendar-date-panel']/div[2]/div[1]/div/input")
input_datetime.send_keys("2021-09-06")
time.sleep(2)

# 下拉选择违规类型
driver.find_element_by_xpath(
    "//div[@class='table-page-search-wrapper']/form/div[2]/div[1]/div/div[2]/div/span").click()
time.sleep(2)
# 下拉行为动作、语音、仪容仪表
driver.find_element_by_xpath("//div[@class='ant-select-dropdown-content']/ul/li[1]").click()
time.sleep(2)

# 下拉选择违规项
driver.find_element_by_xpath(
    "//div[@class='table-page-search-wrapper']/form/div[2]/div[2]/div/div[2]/div/span").click()
time.sleep(2)
# 举手、趴桌、撑头
# driver.find_element_by_xpath("//div[@class='ant-select-dropdown-content']/ul/li[1]").click()
# time.sleep(2)
js_egl = '$(".ant-select-dropdown-content").eq(1).find("ul").find("li").eq(0).click()'

# 查询按钮
driver.find_element_by_xpath(
    "//div[@class='table-page-search-wrapper']/form/div[2]/div[3]/span/button[1]").click()
time.sleep(2)
# 重置按钮
driver.find_element_by_xpath(
    "//div[@class='table-page-search-wrapper']/form/div[2]/div[3]/span/button[2]").click()
time.sleep(2)
# 导出按钮
driver.find_element_by_xpath(
    "//div[@class='table-page-search-wrapper']/form/div[2]/div[3]/span/button[3]").click()
time.sleep(2)
# 全部正确按钮
'''
----1、勾选某一条数据，点击全部正确按钮
'''
js_chose = 'window.TEST_02("body tbody",0,0,"input")'
driver.execute_script(js_chose)
time.sleep(3)
driver.find_element_by_xpath(
    "//div[@class='table-page-search-wrapper']/form/div[2]/div[3]/span/button[4]").click()
time.sleep(2)
print("-------------------正却按钮点击成功--------------------------------")
# 弹窗
driver.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button[2]").click()
time.sleep(2)
# 点击完之后进行相应的查看
'''
1、找到查看的按钮，然后点击查看，
2、弹窗中点击确定，弹窗的页面消失。 大弹窗中的取消，确定按钮。
'''
js_query = 'window.TEST_02("body tbody",13,0,"input")'
driver.execute_script(js_query)
driver.find_element_by_xpath()

# 全部错误按钮

# 统计分析模块 ---当有夏季菜单的时候，在li下面就不是div二十其他的元素需要查看一下。
# driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[3]/a").click()
# time.sleep(2)
# # 机构管理模块
# driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[4]/div").click()
# # 职员管理模块
# driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[5]/div").click()


driver.close()
