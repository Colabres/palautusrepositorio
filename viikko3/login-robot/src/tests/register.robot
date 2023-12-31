*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle2  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  New user registered

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ka#lle  ka#lle123
    Output Should Contain  New user registered

Register With Valid Username And Too Short Password
    Input Credentials  kalle2  k
    Output Should Contain  New user registered

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kalleeee
    Output Should Contain  User with username kalle already exists

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command