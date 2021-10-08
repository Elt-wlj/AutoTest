*** Settings ***
Library           Selenium2Library
Resource          MyResource.robot
Resource          ElementRseource.robot

*** Test Cases ***
百度搜索测试用例
    搜索测试    新闻
    搜索测试    123123
