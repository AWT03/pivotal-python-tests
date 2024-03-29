Feature: Create projects
  Background: preconditions
    Given I login the Pivotal Tracker web application as owner

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
    And I go to AllProjects
    And I verify project_name is displayed on projects_list
    And I verify account is displayed on account_list



  Scenario: Verify that a new project is created by project logo header
    When I go to AllProjects
    And I create a project with
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
    And I go to AllProjects
    And I verify project_name is displayed on projects_list
    And I verify account is displayed on account_list



    Scenario: Verify that a new project is created by main header
    When I click on projects_dropdown_list
    And I create a project with
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
    And I go to AllProjects
    And I verify project_name is displayed on projects_list
    And I verify account is displayed on account_list



  Scenario: Verify that disable tasks property do not allow to edit or create tasks
    When I create a project with
        | key           | value                                |
        | project_name  | (prefix)_project_(current_date_time) |
        | account       | (prefix)_account                     |
        | privacy       | Public                               |
    And I go to ->More
    And I modify project settings with
      | key          | value |
      | enable_tasks | false |
    And I go to ->Stories
    And I click on Add Story
    Then I verify add_task element is not displayed

