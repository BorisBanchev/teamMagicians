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
    Input Text  author  Example1
    Input Text  title  Example2
    Input Text  journal  Example3
    Input Text  year  2000
    Click Button  Save reference
    Page Should Contain  Example1
    Page Should Contain  Example2
    Page Should Contain  Example3
    Page Should Contain  2000

After adding two references there is two references
    Go To  ${HOME_URL}
    Click Link  //a[contains(text(), "Add Reference")]
    Input Text  author  Example1
    Input Text  title  Example2
    Input Text  journal  Example3
    Input Text  year  2000
    Click Button  Save reference
    Click Link  //a[contains(text(), "Add Reference")]
    Input Text  author  Example4
    Input Text  title  Example5
    Input Text  journal  Example6
    Input Text  year  2001
    Click Button  Save reference
    Page Should Contain  Example1
    Page Should Contain  Example2
    Page Should Contain  Example3
    Page Should Contain  2000
    Page Should Contain  Example4
    Page Should Contain  Example5
    Page Should Contain  Example6
    Page Should Contain  2001

After adding invalid reference there is no references
    Go To  ${HOME_URL}
    Click Link  //a[contains(text(), "Add Reference")]
    Input Text  author  Example1
    Input Text  title  Example2
    Input Text  journal  Example3
    Input Text  year  2026
    Click Button  Save reference
    Page Should Contain  smaller than 2026
    Click Button  Cancel
    Page Should Contain  No references.

