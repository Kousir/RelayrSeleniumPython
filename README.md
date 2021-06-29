# RelayrSeleniumPython
Hybrid framework on top of Pytest for automation of google search UI 

Objective
=====
The main objective is to test the search UI & functionality of www.google.de 


How test data are handled
=====
Input data (search key) is obtained from excel file. "Openpyxl" package is used in this project.
A separate excelhandler.py file has been added in the utility dir which can be used to get data like row count, column number, etc
'Config.ini' file holds information like webpage/server. Configparser method is used to feel data to test suite


Debugging
=====
Logger pacakge is used to provide info logs along with date & time details 
Logger setup is maintaied as static method in the utility dir. 


Webdriver setup
=====
Webdriver setup is maintain in conftest.py pacakge in the testcase dir 
Chrome functionalites such as permission for mic, camera, notification, etc are handled using options in the conftest.py package
Simple if, else & elif can be added to run the code in runtime browser

Others
=====
Javascript, ActionChains, Chromeoptions & many other codes have been used in the framework
