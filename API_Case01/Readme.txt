API Test - Pablo Calderón J.

This follow steps let verify the API by sing up and login in some scenarios:

1. Sing Up url: https://api.demoblaze.com/signup

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

   There are two test scenarios to sing up API:
	• Create a new user
	• Create a duplicate user


2. Log In url: https://api.demoblaze.com/login

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

   There are three test scenarios to log in API:
	• Give a wrong username
	• Give a wrong password
	• Give the correct information