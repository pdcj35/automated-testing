Feature: APITest

  Scenario Outline: test <SingUpTestCase>
    Given url 'https://api.demoblaze.com/signup'
    When request {"<username>": <TestUsername>,"<password>": <TestPassword>}
    And method POST
    And match response.errorMessage == <errorMessage>
    Then status 200
    Examples:
    |SingUpTestCase |username|TestUsername  |password|TestPassword|errorMessage              |
    |SingUpCorrect  |username|"Test_user023"|password|"TestPsw"   |null                      |
    |SingUpDuplicate|username|"Test_user023"|password|"TestPsw"   |"This user already exist."|

  Scenario Outline: test <LogInTestCase>
    Given url 'https://api.demoblaze.com/login'
    When request {"<username>": <TestUsername>,"<password>": <TestPassword>}
    And method POST
    And match response.errorMessage == <errorMessage>
    Then status 200
    Examples:
      |LogInTestCase     |username|TestUsername  |password|TestPassword|errorMessage          |
      |LogInWrongUserName|username|"Test_user20" |password|"TestPsw"   |"User does not exist."|
      |LogInWrongPassword|username|"Test_user023"|password|"TestPs00"  |"Wrong password."     |
      |LogInCorrectAccess|username|"Test_user023"|password|"TestPsw"   |null                  |
