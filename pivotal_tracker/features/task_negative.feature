Feature: Task Negative cases

  Background: Task preconditions
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

  @corner_case
  Scenario: Create a Task with description field more than allowed
    When I send a POST request to tasks with data in task.json
    Then I expect this error set_more_chars is thrown

  @negative_case
  Scenario: Create a Task with description field empty
    When I send a POST request to tasks with data
  '''
  {
  "description": "",
  "complete": "false",
  "position": "1"
  }
  '''
    Then I expect this error set_empty_description_field is thrown

  @corner_case
  Scenario: Try to create a Task in a position more longer than the current stories' tasks size plus 1
    When I send a POST request to tasks with data
  '''
  {
  "description": "prefix)_project_(current_date_time)",
  "complete": "false",
  "position": "2"
  }
  '''
    Then I expect this error set_position_more_than_size is thrown

  @corner_case
  Scenario: Try to create a Task in position 0
    When I send a POST request to tasks with data
  '''
  {
  "description": "prefix)_project_(current_date_time)",
  "complete": "false",
  "position": "0"
  }
  '''
    Then I expect this error set_position_low_or_equal_zero is thrown

  @corner_case
  Scenario: Try to create a Task in a negative position
    When I send a POST request to tasks with data
  '''
  {
  "description": "prefix)_project_(current_date_time)",
  "complete": "false",
  "position": "-1"
  }
  '''
    Then I expect this error set_position_low_or_equal_zero is thrown

  @corner_case
  Scenario: Try to create a Task with chars in position instead of Integer number
    When I send a POST request to tasks with data
  '''
  {
  "description": "prefix)_project_(current_date_time)",
  "complete": "false",
  "position": "task"
  }
  '''
    Then I expect this error set_chars_in_position is thrown

  @corner_case
  Scenario: Try to create a Task in a position with float number instead of Integer
    When I send a POST request to tasks with data
  '''
  {
  "description": "prefix)_project_(current_date_time)",
  "complete": "false",
  "position": "1.25"
  }
  '''
    Then I expect this error set_chars_in_position is thrown