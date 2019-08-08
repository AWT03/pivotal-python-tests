# Created by gabriel at 23/7/19
Feature: Accounts general management
  # Enter feature description here
  Background: Basic initial steps
    Given I login the Pivotal Tracker web application as owner

  @functional
  Scenario: Verify account default values upon creation are the expected
    When I go to Profile->Accounts
    And I create an account with name (prefix)_account_(current_date_time)
    Then I verify that Current Plan is displayed as Free
    And I go to ->AccountMembers
    And I verify that I am the owner of the account
    And I go to ->Settings
    And I verify account_name is displayed on Account Name
    And I click on delete this account
