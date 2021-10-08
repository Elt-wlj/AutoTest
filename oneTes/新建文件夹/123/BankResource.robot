*** Settings ***
Resource          ElementResource.robot

*** Keywords ***
搜索测试
    [Arguments]    ${search}
    打开浏览器    http://192.168.1.37/user/login
    输入关键字
    点击
    关闭浏览器
