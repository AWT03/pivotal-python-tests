@wip
Feature: Tasks

  Background: Tasks preconditions
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with data
  '''
  {"name": "(prefix)_project_(current_date_time)",
  "account_id": "(current_account_id)"}
  '''
    And I send a POST request to stories with data
  '''
  {"name": "(prefix)_story_(current_date_time)"}
  '''

  # Basic operations
  @acceptance
  Scenario: Create a Task
    When I send a POST request to tasks with data
  '''
  {
  "description": "(prefix)_task_(current_date_time)",
  "complete": "false",
  "position": "1"
  }
  '''
    Then I expect status code is 200
    And I expect the single response contains
  '''
  {
  "description": "(prefix)_task_(current_date_time)",
  "complete": "false",
  "position": "1"
  }
  '''
    And I expect the response id is not null

  @functional
  Scenario: Task GET all tasks in story
    Given I send a POST request to tasks with data
      | description            | complete | position |
      | (prefix)_task_(random) | false    | 1        |
      | (prefix)_task_(random) | false    | 2        |
      | (prefix)_task_(random) | false    | 3        |
    When I send a GET request to tasks
    Then I expect status code is 200
    And I expect the response list contains 3 values
    And I expect the items' ids obtained are equal to the items' ids created before
    And I expect the items' value obtained are equal to the items' value created before

  @functional
  Scenario Outline: Create a Task with different ways to set up the complete field
    When I send a POST request to tasks with data
      | description   | complete   | position   |
      | <description> | <complete> | <position> |
    Examples:
      | description   | complete   | position   |
      | (prefix)_task_(random) | false | 1 |
      | (prefix)_task_(random) | true | 1 |

