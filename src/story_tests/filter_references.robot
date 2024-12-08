*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
Filter references
    Go To  ${HOME_URL}
    Click Link  //a[contains(text(), "Add Reference")]
    Select From List By Label  reference_type  Article
    Input Text  author  Example1
    Input Text  title  Example2
    Input Text  journal  Example3
    Input Text  year  2000
    Input Text  keyword  article
    Click Button  Save Reference
    Click Link  //a[contains(text(), "Add Reference")]
    Select From List By Label  reference_type  Article
    Input Text  author  Example4
    Input Text  title  Example5
    Input Text  journal  Example6
    Input Text  year  2001
    Input Text  keyword  article2
    Click Button  Save Reference
    Page Should Contain  Example1
    Page Should Contain  Example2
    Page Should Contain  Example3
    Page Should Contain  2000
    Page Should Contain  Example4
    Page Should Contain  Example5
    Page Should Contain  Example6
    Page Should Contain  2001
    Input Text  id=searchbox  Example1
    Element Should Be Visible  //tr[contains(@class, "reference_row")]//span[contains(text(), "Example1")]
    Element Should Be Visible  //tr[contains(@class, "reference_row")]//span[contains(text(), "Example2")]
    Element Should Be Visible  //tr[contains(@class, "reference_row")]//span[contains(text(), "Example3")]
    Element Should Be Visible  //tr[contains(@class, "reference_row")]//span[contains(text(), "2000")]
    Element Should Not Be Visible  //tr[contains(@class, "reference_row")]//span[contains(text(), "Example4")]
    Element Should Not Be Visible  //tr[contains(@class, "reference_row")]//span[contains(text(), "Example5")]
    Element Should Not Be Visible  //tr[contains(@class, "reference_row")]//span[contains(text(), "Example6")]
    Element Should Not Be Visible  //tr[contains(@class, "reference_row")]//span[contains(text(), "2001")]
    