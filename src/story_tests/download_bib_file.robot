*** Settings ***
Resource  resource.robot
Library   OperatingSystem
*** Test Cases ***
Download BibTeX File
    [Documentation]  
    Open And Configure Browser
    Go To  ${HOME_URL}
    Add Reference
    Render BibTeX And Download File
    Close Browser

*** Keywords ***
Add Reference
    [Documentation]    Add a reference to the system
    Click Link  //a[contains(text(), "Add Reference")]
    Select From List By Label  reference_type  Article
    Input Text  author  Example1
    Input Text  title  Example2
    Input Text  journal  Example3
    Input Text  year  2000
    Input Text  keyword  article
    Click Button  Save Reference
    Sleep  1s  # Wait for the reference to be added and redirected to the home page
    Page Should Contain  Example1
    Page Should Contain  Example2
    Page Should Contain  Example3
    Page Should Contain  2000
Render BibTeX And Download File
    [Documentation]    Render BibTeX and download the file
    Click Link  Render BibTeX
    Sleep  5s  # Wait for the BibTeX to be rendered
    Click Button  Download BibTeX file
    Sleep  10s  # Wait for the download to complete
    ${downloaded_file}  Run Keyword And Return Status  File Should Exist  ${OUTPUT_DIR}/references.bib
    Log  Downloaded file exists: ${downloaded_file}
    Should Be True  ${downloaded_file}