Feature: Task Corner and Negative cases

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
    And I send a POST request to tasks with data
  '''
  {
  "description": "(prefix)_task_(current_date_time)",
  "complete": "false",
  "position": "1"
  }
  '''

  @task @corner_case
  Scenario Outline: Verify that I can not update a Task with description empty and position with different invalid values
    When I send a PUT request to tasks with data
      | description   | complete   | position   | error   |
      | <description> | <complete> | <position> | <error> |
    Then I expect this error <error> is thrown
    Examples:
      | description               | complete | position | error                                |
      |                           | false    | 1        | set_empty_description_field          |
      | (prefix)_project_(random) | false    | 2        | set_position_more_than_size_updating |
      | (prefix)_project_(random) | false    | 0        | set_position_low_or_equal_zero       |
      | (prefix)_project_(random) | false    | -1       | set_position_low_or_equal_zero       |
      | (prefix)_project_(random) | false    | 1.25     | set_chars_in_position                |
      | (prefix)_project_(random) | false    | task     | set_chars_in_position                |
