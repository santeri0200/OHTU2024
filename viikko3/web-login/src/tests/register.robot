*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  esa
    Set Password  esa12345
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  es
    Set Password  esa12345
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  esa
    Set Password  esa1234
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  esa
    Set Password  esapitka
    Submit Credentials
    Register Should Fail With Message  Password should contain numbers and/or special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  esa
    Set Password  esa12345
    Input Text  password_confirmation  esa12346
    Submit Credentials
    Register Should Fail With Message  Password and the confirmation do not match

Register With Username That Is Already In Use
    Create User  kalle  kalle123
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}
    Input Text  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
