*** Settings ***
Library           Selenium2Library
Resource          MyResourceLogin.txt
Resource          ElementResource.txt

*** Test Cases ***
登陆测试用例
    输入用户名    admin
    输入密码    123456
