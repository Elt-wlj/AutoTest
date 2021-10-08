*** Keywords ***
LoginTest
    [Arguments]    ${search}
    Open Browser    http://192.168.1.37/user/login    gc
    Input Text    xpath=//*[@id='username']    admin
    Input Password    xpath=//*[@id='password']    123456
    Click Button    xpath=//*[@id='formLogin']/div/div[3]/div/div/span/button
    Wait Until Element Is Visible    xpath=//*[@id='username']
    Close Browser    #关闭浏览器
