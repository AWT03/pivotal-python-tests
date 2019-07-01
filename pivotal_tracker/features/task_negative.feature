Feature: Task Negative cases

  Background: Task preconditions
    Given I start a connection with the API
    And I log in as user owner
    And I send a "POST" request to "projects" with data
  '''
  {"name": "(prefix)_project_(current_date_time)",
  "account_id": "(current_account_id)"}
  '''
    And I send a "POST" request to "stories" with data
  '''
  {"name": "(prefix)_story_(current_date_time)"}
  '''

  Scenario: Create a Task with description field more than allowed
    When I send a "POST" request to "tasks" with data in "task.json"
    Then I expect the code is "invalid_parameter"

  Scenario: Create a Task with description field empty
    When I send a "POST" request to "tasks" with data in "task_empty.json"
    Then I expect the code is "invalid_parameter"

