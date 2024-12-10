*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
After fetching by DOI succesfully, there is a reference
    Go To  ${HOME_URL}
    Title Should Be  Reference App
    Page Should Contain  No references.
    Click Link  //a[contains(text(), "Add Reference")]
    Input Text  doi_fetch  https://dl.acm.org/doi/10.1145/3678698.3687185
    Click Button  Fetch Reference
    Input Text  keyword  doitest
    Click Button  Save Reference
    Wait Until Page Contains  doitest  timeout=10s
    Wait Until Page Contains  Canet Sola
    Wait Until Page Contains  Visions of Destruction