
from login import Login_open

Login_open()
# 评估质量审核页面
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[5]/a").click()
time.sleep(2)
# 左侧组织树的搜索
# js_zzs = 
driver.execute_script('$("input:eq(0)").val("光华")')
# 输入员工的姓名
driver.execute_script('$("input:eq(1)").val("金文莉")')
# driver.find_element_by_xpath("//div[@class='table-page-search-wrapper']/form/div/div[1]/div/div[2]/div/span/input").send_keys('金文莉')
time.sleep(2)
# 输入员工的工号
driver.execute_script('$("input:eq(2)").val("007480")')
# driver.find_element_by_xpath("//div[@class='table-page-search-wrapper']/form/div/div[2]/div/div[2]/div/span/input").send_keys('007480')
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
driver.execute_script(js_egl)
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
# rint("-------------------正确按钮点击成功--------------------------------")
# 弹窗
driver.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button[2]").click()
time.sleep(2)
# 点击完之后进行相应的查看
'''
1、找到查看的按钮，然后点击查看，
2、弹窗中点击确定，弹窗的页面消失。 大弹窗中的取消，确定按钮。
'''
js_query = 'window.TEST_02("body tbody",0,0,"input")'
driver.execute_script(js_query)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[13]/span/a').click()
# print('-------------查看按钮点击成功----------------------')
time.sleep(2)
# 点击弹窗的确定按钮
driver.find_element_by_xpath("//div[@class='ant-modal-content']/div[3]/div/button[2]").click()
time.sleep(2)
# 页数的跳转 ---输入5页
driver.find_element_by_xpath("//div[@class='ant-pagination-options-quick-jumper']/input").send_keys('5')
time.sleep(2)
# 获取键盘上的enter数据
driver.find_element_by_xpath("//div[@class='ant-pagination-options-quick-jumper']/input").send_keys(Keys.ENTER)
# 点击向左的方像箭头
js_left = '$(".ant-pagination-item-link").find(".anticon.anticon-left").click()'
driver.execute_script(js_left)
time.sleep(2)
# 点击向右的箭头
js_right= '$(".ant-pagination-item-link").find(".anticon.anticon-right").click()'
driver.execute_script(js_right)
time.sleep(2)

#统计分析模块 ---当有夏季菜单的时候，在li下面就不是div二十其他的元素需要查看一下。
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[3]/a").click()
time.sleep(2)
# 机构管理模块
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[4]/div").click()
# 职员管理模块
driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[5]/div").click()


driver.close()