Feature: Create projects
  Background: preconditions
    Given I login the app as owner

  Scenario: Verify that new projects are displayed correctly
    When I create a project with
        | key           | value                                |
        | project_name  | (prefix)_project_(current_date_time) |
        | account       | (prefix)_account                     |
        | privacy       | public                               |
    Then I verify project_name is displayed on header_name
#    And I verify privacy is displayed on header_name
    And I go to ProjectMain->More
    And I verify project settings were created according to characteristics
    And I go to Dashboard->Projects
    And I verify project_name is displayed on projects_dashboard
#    And I verify privacy is displayed on project_dashboard
#    And I verify my projects counter is counting all projects
    And I go to AllProjects
    And I verify project_name is displayed on projects_list
#    And I verify account is displayed on project_list
#    And I go to Accounts
#    And I verify project_name is displayed on current_account
