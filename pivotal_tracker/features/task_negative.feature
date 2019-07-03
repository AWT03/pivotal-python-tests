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

#  @corner_case
#  Scenario: Create a Task with description field more than allowed
#    When I send a POST request to tasks with data in task.json
#    Then I expect this error set_more_chars is thrown

  @negative_case
  Scenario Outline: Create a Task with different ways two set up the complete field
    When I send a "POST" request to "tasks" with data "<description>" "<complete>" "<position>"
    Examples:
      | description   | complete   | position   |
      | (prefix)_task_(current_date_time) | false | 1 |
      | (prefix)_task_(current_date_time) | true | 1 |

  @negative_case
    Scenario Outline: Create a Task with  description field empty
    When I send a POST request to tasks with data
      | description   | complete   | position   |error|
      | <description> | <complete> | <position> |<error>|
    Examples:
      | description                         | complete | position | error                          |
      |                                     | false    | 1        | set_empty_description_field    |
      | prefix)_project_(current_date_time) | false    | 2        | set_position_more_than_size    |
      | prefix)_project_(current_date_time) | false    | 0        | set_position_low_or_equal_zero |
      | prefix)_project_(current_date_time) | false    | -1       | set_position_low_or_equal_zero |
      | prefix)_project_(current_date_time) | false    | 1.25     | set_chars_in_position          |
      | prefix)_project_(current_date_time) | false    | task     | set_chars_in_position          |

#  @negative_case
#    Scenario Outline: Create a Task with description field empty
#    When I send a POST request to tasks with data
#      | description   | complete   | position   |
#      | <description> | <complete> | <position> |
#    Then I expect this error <error> is thrown
#    Examples:
#      | description                         | complete | position | error                          |
#      |                                     | false    | 1        | set_empty_description_field    |
#      | prefix)_project_(current_date_time) | false    | 2        | set_position_more_than_size    |
#      | prefix)_project_(current_date_time) | false    | 0        | set_position_low_or_equal_zero |
#      | prefix)_project_(current_date_time) | false    | -1       | set_position_low_or_equal_zero |
#      | prefix)_project_(current_date_time) | false    | 1.25     | set_chars_in_position          |
#      | prefix)_project_(current_date_time) | false    | task     | set_chars_in_position          |

#  @negative_case
#  Scenario: Create a Task with description field empty
#    When I send a POST request to tasks with data
#  '''
#  {
#  "description": "",
#  "complete": "false",
#  "position": "1"
#  }
#  '''
#    Then I expect this error set_empty_description_field is thrown
#
#  @corner_case
#  Scenario: Try to create a Task in a position more longer than the current stories' tasks size plus 1
#    When I send a POST request to tasks with data
#  '''
#  {
#  "description": "prefix)_project_(current_date_time)",
#  "complete": "false",
#  "position": "2"
#  }
#  '''
#    Then I expect this error set_position_more_than_size is thrown
#
#  @corner_case
#  Scenario: Try to create a Task in position 0
#    When I send a POST request to tasks with data
#  '''
#  {
#  "description": "prefix)_project_(current_date_time)",
#  "complete": "false",
#  "position": "0"
#  }
#  '''
#    Then I expect this error set_position_low_or_equal_zero is thrown
#
#  @corner_case
#  Scenario: Try to create a Task in a negative position
#    When I send a POST request to tasks with data
#  '''
#  {
#  "description": "prefix)_project_(current_date_time)",
#  "complete": "false",
#  "position": "-1"
#  }
#  '''
#    Then I expect this error set_position_low_or_equal_zero is thrown
#
#  @corner_case
#  Scenario: Try to create a Task with chars in position instead of Integer number
#    When I send a POST request to tasks with data
#  '''
#  {
#  "description": "prefix)_project_(current_date_time)",
#  "complete": "false",
#  "position": "task"
#  }
#  '''
#    Then I expect this error set_chars_in_position is thrown
#
#  @corner_case
#  Scenario: Try to create a Task in a position with float number instead of Integer
#    When I send a POST request to tasks with data
#  '''
#  {
#  "description": "prefix)_project_(current_date_time)",
#  "complete": "false",
#  "position": "1.25"
#  }
#  '''
#    Then I expect this error set_chars_in_position is thrown