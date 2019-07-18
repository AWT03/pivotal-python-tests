Feature: Create projects
  Background: preconditions
    Given I login the app as owner

  Scenario: Verify that new projects are created correctly
    When I create a project with characteristics
        | key           | value                                |
        | project_name  | (prefix)_project_(current_date_time) |
        | account       | (prefix)_account                     |
        | privacy       | public                               |
    Then I verify project name is displayed in header
    And I verify that project settings were created according to characteristics
    And I verify that project name is on dashboard
    And I verify that project is on projects menu
