*** Settings ***
Test Setup
Test Teardown
Test Template
Library           Selenium2Library
Resource          JJResource.txt

*** Test Cases ***
JJtestCase
    LoginSuccess

LoginFailTest
    LoginTestFail

BussenQula
    业务质量模块

CountAnalyse
    统计分析页

InstitManage
    机构管理页

if语句
    Comment    ${var}    Set Variable    admin
    Comment    Run Keyword if    '${var}'=='123456    log    用户名为admin
    Comment    ...
    ...    ELSE    log    用户名错误
    Comment    Index

EmployeeManager
    职员管理

LanguagManage
    语言规范管理

EquipManager
    设备管理页

wanglaoshi
    测试用

ScenceManager
    场景管理

PsmLog
    PSM客户机日志

Pagejump
    页面数据页的跳转

AlgorithmBox
    算法盒子管理

UpgradeMa
    升级管理

ServiceTotal
    服务质量总表

AppealManage
    申诉处理页

AppealResult
    申述结果页

SystemManage
    系统管理页

SyM_StataManage
    系统_岗位管理

UserManage
    用户管理

MyNews
    我的消息

SysInformation
    系统通告

EvaluateResult
    评估结果审核
