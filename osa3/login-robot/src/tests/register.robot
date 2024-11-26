*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  valid  valid
    Output Should Contain  Register successful