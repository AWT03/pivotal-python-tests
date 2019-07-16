Feature: Projects

  Background: Preconditions
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a GET request to projects
    And I count how many projects are already created

  @functional
  Scenario: Verify that I can create a multiple projects in an account
    When I send a POST request to projects with data
      | name                                |
      | (prefix)_multiple_projects_(random) |
      | (prefix)_multiple_projects_(random) |
      | (prefix)_multiple_projects_(random) |
    When I send a GET request to projects
    Then I expect status code is 200
    And I expect the response list contains 3 values
    And I expect the items' ids obtained are equal to the items' ids created before

  @functional
  Scenario Outline: Verify that I can create projects with different project_type
    When I send a POST request to projects with data
      | name   | project_type   |
      | <name> | <project_type> |
    Then I expect status code is 200
    Examples:
      | name                      | project_type |
      | (prefix)_project_(random) | public       |
      | (prefix)_project_(random) | private      |

  @functional
  Scenario Outline: Verify that "start date" of projects match with correct "day of the week start"
    When I send a POST request to projects with data
      | name   | week_start_day   | start_date   |
      | <name> | <week_start_day> | <start_date> |
    Then I expect status code is 200
    Examples:
      | name                      | week_start_day | start_date |
      | (prefix)_project_(random) | Monday         | 2019-07-15 |
      | (prefix)_project_(random) | Tuesday        | 2019-07-16 |
      | (prefix)_project_(random) | Wednesday      | 2019-07-17 |
      | (prefix)_project_(random) | Thursday       | 2019-07-18 |
      | (prefix)_project_(random) | Friday         | 2019-07-19 |


  @acceptance
  Scenario: Verify that I can create a Project
    When I send a POST request to projects with data
  '''
  {
  "name": "(prefix)_project_(current_date_time)"
  }
  '''
    Then I expect status code is 200
    And I expect the single response contains
  '''
  {
  "name": "(prefix)_project_(current_date_time)"
  }
  '''
    And I expect the response id is not null

  @functional
  Scenario: Verify that I can get all projects
    When I send a GET request to projects
    Then I expect the response is a list
    And I expect status code is 200

  @functional
  Scenario: Verify that I can create a Project with all fields
    When I send a POST request to projects with data
  '''
  {
  "name": "(prefix)_project_(current_date_time)",
  "public": "true",
  "iteration_length": "2",
  "week_start_day": "Monday",
  "point_scale": "0,1,2,3",
  "enable_tasks": "true",
  "project_type": "private",
  "enable_incoming_emails": "true"
  }
  '''
    Then I expect status code is 200

  @corner_case
  Scenario: Verify that I can not create a Project with name larger than 50 characters
    When I send a POST request to projects with data from project.json
    Then I expect status code is 400
    And I expect this error too_large_name is thrown

  @functional
  Scenario: Verify that I can create a project with "public" attribute to be visible for all
    When I send a POST request to projects with data
  '''
  {
  "name": "(prefix)_project_(current_date_time)",
  "public": "true"
  }
  '''
    And I log in as user member1
    And I send a GET request to projects
    Then I expect status code is 200