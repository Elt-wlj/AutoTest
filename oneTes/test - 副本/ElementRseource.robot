*** Keywords ***
打开浏览器
    [Arguments]    ${url}
    Open Browser    ${url}    chrome

输入关键字
    [Arguments]    ${search}
    Input text    xpath=//*[@id='username']    admin
    Input text    xpath=//*[@id='password']    123456

点击搜索
    Click Button    xpath=.//*[@id='formLogin']/div/div[3]/div/div/span/button
    Sleep    2

关闭浏览器
    Close Browser    # 关闭浏览器
