*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
At start there are no references
    Go To  ${HOME_URL}
    Title Should Be  Reference App
    Page Should Contain  No references.

After adding a reference, there is one
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

After adding two references there is two references
    Go To  ${HOME_URL}
    Click Link  //a[contains(text(), "Add Reference")]
    Select From List By Label  reference_type  Article
    Input Text  author  Example21
    Input Text  title  Example22
    Input Text  journal  Example23
    Input Text  year  2000
    Input Text  keyword  article 
    Click Button  Save Reference
    Click Link  //a[contains(text(), "Add Reference")]
    Select From List By Label  reference_type  Article
    Input Text  author  Example24
    Input Text  title  Example25
    Input Text  journal  Example26
    Input Text  year  2001
    Input Text  keyword  article2
    Click Button  Save Reference
    Page Should Contain  Example21
    Page Should Contain  Example22
    Page Should Contain  Example23
    Page Should Contain  2000
    Page Should Contain  Example24
    Page Should Contain  Example25
    Page Should Contain  Example26
    Page Should Contain  2001

After adding invalid reference there is no references
    Go To  ${HOME_URL}
    Click Link  //a[contains(text(), "Add Reference")]
    Select From List By Label  reference_type  Article
    Input Text  author  Example1
    Input Text  title  Example2
    Input Text  journal  Example3
    Input Text  year  2027
    Input Text  keyword  article 
    Click Button  Save Reference
    Alert Should Be Present  Reference year must be positive and smaller than 2026

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
    Click Button  Delete
    Page Should Contain  No references.