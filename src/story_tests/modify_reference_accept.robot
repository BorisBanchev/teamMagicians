
*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos


*** Test Cases ***
Modify Added Reference
    Add Reference    Example1    Example2    Exaple3    2000    article1
    Click Button  id=modify
    Input Text  journal  Example3
    Click Button  Save Changes
    Page Should Contain  Example3

Start Modifying Reference and Then Cancel Changes
    Add Reference    Example1    Example2    Exaple3    2000    article1
    Click Button  id=modify
    Input Text  journal  Example3
    Click Button  Cancel
    Page Should Contain  Exaple3

Receive Alert When Saving Changes With a Future Year
    Add Reference    Example1    Example2    Example3    2000    article1
    Click Button  id=modify
    Input Text  year  2050
    Click Button  Save Changes
    Alert Should Be Present  Reference year must be positive and smaller than 2025

*** Keywords ***
Add Reference
    [Arguments]    ${author}    ${title}    ${journal}    ${year}    ${keyword}
    Go To  ${HOME_URL}
    Click Link  //a[contains(text(), "Add Reference")]
    Select From List By Label  reference_type  Article
    Input Text  author  ${author}
    Input Text  title  ${title}
    Input Text  journal  ${journal}
    Input Text  year  ${year}
    Input Text  keyword  ${keyword}
    Click Button  Save Reference
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${journal}
    Page Should Contain  ${year}
