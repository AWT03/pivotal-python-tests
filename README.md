# Pivotal Tests


## Overview

[![Build status](https://travis-ci.com/AWT03/pivotal-tests.svg?branch=develop)](https://travis-ci.com/AWT03/pivotal-tests) 

[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=AWT03_pivotal-tests&metric=alert_status)](https://sonarcloud.io/dashboard/index/AWT03_pivotal-tests)


This project's objective is to set up some testing for the Pivotal Tracker API.

## Requirements

This project was intended to work with python 3.6. A list of required libraries can be found on "requirements.txt" file.
 
* behave
* request
* simplejson
* selenium
* webdriver-manager

This means all required libraries can be installed from the project path using:
```sh 
pip3 install -r requirements.txt
```
## About the project

On the 'core' folder we intend to put generic steps and functions that can be used on any API testing. 
We also included a generic API request class, this class can be inherited to customize request options.

## Setting Up 
## PIVOTAL TRACKER API Testing

Go to "pivotal_tracker/api" folder inside the project directory.
There you will find a "config.dist" file (Configurations are based on json file format). 
This file contains all the configuration that will be used for the API testing.
It should be filled as indicated (all examples are based on APIv5):

* "BASE_URL": The pivotal tracker API URL (e.g. "https://www.pivotaltracker.com/services/v5")
* "TOKEN_HEADER": This is the name of the header that will contain the token (e.g. "X-TrackerToken")
* "PREFIX": This prefix will be used on all created projects and also to delete all data that was generated by testing tool.
* "USER": This is a list of users. By default it expects one owner and two members (working on the same account). 
You can find your user TOKEN and ID on the User settings in Pivotal Tracker page (e.g. "https://www.pivotaltracker.com/profile"). 
If you don't find the id you can always request it.
* "ACCOUNT_ID": The account id the users are working on. It can be found on the account settings.
* "PATH_DATA_FILES": You can use customized test data. If you don't know how to configure this or what files are required 
you can fill this with "/pivotal_tracker/api/features/test_data". If customized testing is being done please create all files for testing.
* "Content-Type": This depends on the type of request we are sending. If not customized please use "application/java".

After filling all these field you can change the configuration file name "config.dist" -> "config.json". 
Once we do this we are good to go for some testing.

To run features you have to go to the project path and run:
```sh 
behave pivotal_tracker/api/features --verbose
```
To run only features marked with a certain tag like "@acceptance" or "@functional":
```sh 
behave pivotal_tracker/api/features -t acceptance
behave pivotal_tracker/api/features -t functional
```
You can check the behave for better understanding of the tool, [click here](https://behave.readthedocs.io/en/stable/).

## Generate the Report

To generate the report make sure have installed the following:
```sh 
allure-behave
allure 2.12.1
java 1.8.0_201
```
You can check the folllowing link [click here](https://docs.qameta.io/allure/#_get_started) for doing that.

Then on terminal execute these commands:
```sh 
behave -f allure_behave.formatter:AllureFormatter -o ./pivotal_tracker/api/allure/results ./pivotal_tracker/api/features
allure serve ./pivotal_tracker/api(allure/results
```
Finally a web page with the report should be displayed on the browser.

## PIVOTAL TRACKER GUI Testing
Go to "pivotal_tracker/ui" folder inside the project directory.
There you will find a "config.dist" file (Configurations are based on json file format). 
This file contains all the configuration that will be used for the GUI testing.
It should be filled as indicated:

* "BROWSER": The browser we will use for testing (e.g. "firefox", "chrome").
* "INITIAL_PAGE": This is the initial login page: "https://www.pivotaltracker.com/signin". 
* "PREFIX": This prefix will be used on all created projects and also to delete all data 
that was generated by testing tool (e.g. "AWT03").
* "USER": This is a list of users. By default it expects one owner. 
You must use a correct account username/email and password.

To check all GUI tests you can run the command on project directory:
```sh 
behave pivotal_tracker/ui/features
```
