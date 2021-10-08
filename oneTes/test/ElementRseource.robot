*** Keywords ***
打开浏览器
    [Arguments]    ${url}
    Open Browser    ${url}    chrome

输入关键字
    [Arguments]    ${search}
    Input text    xpath=//*[@id="kw"]    ${search}

点击搜索
    Click Button    id=su
    Sleep    2

效验标题
    [Arguments]    ${result}
    ${title}    GET Title
    Should Contain    ${title}    ${result}

关闭浏览器
    Close Browser    # 关闭浏览器
