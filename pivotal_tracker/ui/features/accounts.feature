# Created by gabriel at 23/7/19
Feature: Accounts general management
  # Enter feature description here
  Background: Basic initial steps
    Given I login the app as owner

  Scenario: Create a new account and delete it
    When I go to Profile->Accounts
    And I create an account with name (prefix)_account_(current_date_time)
    And I go to Profile->Accounts->AccountsList
    And I select Manage Account for recently created
    And I go to ->Settings
    And I click on delete this account
