HOW TO:

1. Overview of all the files in Test Automation package:
	- HowTo.txt 					-> detailed explanation of Test Automation package
	- requirements.txt 				-> package requirements that needs to be installed
	- setup.py					-> setup script
	- gist_test_suite:				
		- test_suite.py				-> main automation script
		- utilities.py				-> additional utilities
		- execute.bat				-> batch file for test suite execution
		- setup_script.bat			-> batch file for installing all required packages
		- input_files:
			- PublicGist.json		-> Json file for creating Gist content
		
2. Overview of the language / framework used:
	- Python language is used to develop test automation
	- xUnit testing framework "pytest" is used to create test suite
	- When test automation is executed, user will be prompt to enter the type of token with different privelegies before test case execution: Unauthorized, Public or Authorized.
	- After entering type of token test cases will be executed for testing GIST REST API.
	- After execution is finished, Report with detailed analysis will be generated in the "output_files" folder

3. How to set up dependencies and environment for the project:
	- install python 3.8 and set up PATH in environment variables for python
	- install pip and set up PATH in environment variable for pip
	- downlaod all the files from "https://github.com/PetarJovancic/gist-test-suite" into "C:\gist_test_suite\" directory
	- install required packages by executing "setup_script.bat" 	NOTE: required package are listed in the "requirements.txt"
	- NOTE: if different folder structure is created than the defult one, please make sure to change folder directories in "utilities.py" and "execute.bat"

4. How to execute the tests from command line:
	- Execution of tests can be done by simply executing "execute.bat" script
	- Reports will be generated in the folder "output_files"
	- Json output files will be also generated in the folder "output_files"