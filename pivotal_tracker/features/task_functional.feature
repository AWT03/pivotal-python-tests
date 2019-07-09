Feature: Task

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

  @task @acceptance
  Scenario: Verify that I can get a specific Task's information
    When I send a GET request to tasks
    Then I expect status code is 200
    And I expect the single response contains
  '''
  {
  "description": "(prefix)_task_(current_date_time)",
  "complete": "false",
  "position": "1"
  }
  '''

  @task @acceptance
  Scenario: Verify that I can modify a specific Task's values
    When I send a PUT request to tasks with data
  '''
  {
  "description": "(prefix)_new_description_(current_date_time)",
  "complete": "true",
  "position": "1"
  }
  '''
    Then I expect status code is 200
    And I expect the single response contains
  '''
  {
  "description": "(prefix)_new_description_(current_date_time)",
  "complete": "true",
  "position": "1"
  }
  '''

  @task @acceptance
  Scenario: Verify that I can delete a Task
    When I send a DELETE request to tasks
    Then I expect status code is 204
    And I send a GET request to tasks
    And I expect this error get_deleted_object is thrown
