Feature: Project

  Background: Precondition
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with data
  '''
  {"name": "(prefix)_project_(current_date_time)"}
  '''
    And I send a POST request to stories with data
  '''
  {"name": "(prefix)_story_(current_date_time)"}
  '''

  @functional
  Scenario: Verify that I can enable to a project for creating tasks
    When I send a PUT request to projects with data
  '''
  {"enable_tasks": "true"}
  '''
    And I send a POST request to tasks with data
  '''
  {"description": "(prefix)_task_(current_date_time)"}
  '''
    Then I expect status code is 200

  @defect
  Scenario: Verify that when Project is disable to create task any task should be possible to create
    When I send a PUT request to projects with data
  '''
  {"enable_tasks": "false"}
  '''
    And I send a POST request to tasks with data
  '''
  {"description": "(prefix)_task_(current_date_time)"}
  '''
    Then I expect status code is 400

