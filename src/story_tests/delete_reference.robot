*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos


*** Test Cases ***

After adding valid reference delete reference
    Go To  ${HOME_URL}
    Click Link  //a[contains(text(), "Add Reference")]
    Select From List By Label  reference_type  Article
    Input Text  author  Example1
    Input Text  title  Example2
    Input Text  journal  Example3
    Input Text  year  2000
    Input Text  keyword  article 
    Click Button  Save Reference
    Page Should Contain  Example1
    Page Should Contain  Example2
    Page Should Contain  Example3
    Page Should Contain  2000
    Click Button  id=delete
    Handle Alert  accept
    Page Should Contain  No references.