# MOBILE_PURCHASE_AUTOMATION

Pre-requisites:
1)Python should be installed and its path should be added to environment variable 
2)Requires installation and import of certain packages : selenium,pytest,time,inspect,logging
3)A steady Internet connection
4)Knowledge of the philosophies of Page Object Mechanism(POM), Object-Oriented Programming System(OOPs), Web Testing Automation and User Friendly Customization

SUMMARY
We have an e-commerce website to purchase phones. We built a data-driven,parameterized framework from scratch using pytest in Selenium, which will ask user for browser choice before execution, select desired cellphone, perform checkout and ultimately display SUCCESS alert on console.
There will be separate folders for all setup and teardown utlities,testcases,logs and reports. The framework developed will leverage the philosophies of Page Object Mechanism(POM), Object-Oriented Programming System(OOPs), Web Testing Automation and User Friendly Customization and execute within minimal time, parallelly updating logs and forming reports for each run, with screenshots attached in case of test failure

TECHNOLOGIES USED
Backend: Python, Selenium, Pytest, HTML
Frontend: Shell Scripting, Website - https://rahulshettyacademy.com/angularpractice/shop

ACHIEVEMENTS
Easy Framework Setup: For this framework, we just need to install python along with selenium and pytest packages.
Reduces Overall Time And Effort: Complete autonomy of frontend user to choose browser, hassle free trigger command that returns test results and validation metrics under 5 minutes
Fast-paced timelines friendly: Mindful usage of Implicit Wait,time.sleep() and Explicit Wait allows testcase to execute, log and generate test summary, all within 5 minutes
Automated Testcase Status Assertion: We used assertions to validate if expected success alert was displayed in the console to ensure that the testcase has passed
Improved Readability: Usage of OOPs and POM philosophies imparts a Divide and Conquer quality to the utility, making each class and their functions more task (or webpage) specific and readable to the developers working with legacy code
Customizable Utilization: Browser selection at runtime, ability to quickly target a specific function in a specific webpage for client requested modifications
Learning Opportunity: We learnt standards of writing Selenium tests in frameworks,creating browser invocation fixtures in conftest.py,setting up base class to hold all common utilities,inheriting base class to all tests to remove fixture redundant code, passing command line options to select browser at runtime,implementing Page Object Mechanism,smarter way of returning page objects from navigation methods,creating Selenium webdriver custom utilities in base class, parameterizing webdriver tests with multiple datasets,organizing data from different datafiles and injecting into fixture at runtime ,implementing logging feature to webdriver tests,test execution's html reporting while building this automated testcase

TRIGGER COMMAND : 
py.test [PYTHON_FILENAME_WITH_LOCATION] -v -s --html=report.html



