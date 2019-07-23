Feature: Create projects
  Background: preconditions
    Given I login the app as owner

    @wip
  Scenario: Verify that new projects are displayed correctly
    When I create a project with
        | key           | value                                |
        | project_name  | (prefix)_project_(current_date_time) |
        | account       | (prefix)_account                     |
        | privacy       | Public                               |
    Then I verify project_name is displayed on header_name
    And I verify privacy is displayed on header_privacy
    And I go to ProjectMain->More
    And I verify project settings were created according to characteristics
    And I go to Dashboard->Projects
    And I verify project_name is displayed on projects_dashboard
    And I verify my projects counter is counting all projects
    And I go to AllProjects
    And I verify project_name is displayed on projects_list
    And I verify account is displayed on account_list


  Scenario: Verify that is not possible to manage tasks in a project when disable this property
    When I create a project with
        | key           | value                                |
        | project_name  | (prefix)_project_(current_date_time) |
        | account       | (prefix)_account                     |
        | privacy       | Public                               |
    And I go to ProjectMain->More
    And I modify project settings with
      | key          | value |
      | enable_tasks | false |
    And I go to ProjectMain->Stories
    And I click on Add Story
    Then I verify add_task element is not displayed
