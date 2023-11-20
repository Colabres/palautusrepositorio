*** Settings ***
Resource  resource.robot
#Resource  login.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  Pavel
    Set Password  Pavel123
    Set Confirmation Password  Pavel123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Pa
    Set Password  Pavel123
    Set Confirmation Password  Pavel123
    Submit Credentials
    Register Should Fail With Message  Username too short
    
Register With Valid Username And Invalid Password
    Set Username  Pavel
    Set Password  Pavel
    Set Confirmation Password  Pavel
    Submit Credentials
    Register Should Fail With Message  Invalid Password

Register With Nonmatching Password And Password Confirmation
    Set Username  Pavel
    Set Password  Pavel123
    Set Confirmation Password  Pavel
    Submit Credentials
    Register Should Fail With Message  Nonmatching Password And Password Confirmation

Login After Successful Registration
    Set Username  Marko
    Set Password  Marko123
    Set Confirmation Password  Marko123
    Submit Credentials
    Go To Login Page
    Set Username  Marko
    Set Password  Marko123
    Submit Credentials2
    Login Should Succeed

Login After Failed Registration
    Set Username  Darko
    Set Password  Darko123
    Set Confirmation Password  Darko123
    Submit Credentials
    Go To Login Page
    Set Username  Darko
    Set Password  Marko123
    Submit Credentials2
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Submit Credentials2
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation Password
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}   

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open    

