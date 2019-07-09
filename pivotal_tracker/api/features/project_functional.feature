Feature: projects

  Background: common log in
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with data
  '''
  {"name": "(prefix)_project_(current_date_time)"}
  '''

  Scenario: Project DELETE
    When I send a DELETE request to projects
    Then I expect status code is 204

  Scenario: Project PUT all fields
    When I send a PUT request to projects with data
  '''
  {"name": "(prefix)_project_(current_date_time)",
  "public": "true",
  "iteration_length": "2",
  "week_start_day": "Monday",
  "point_scale": "0,1,2,3",
  "enable_tasks": "true",
  "project_type": "private",
  "enable_incoming_emails": "true"}
  '''
    Then I expect status code is 200

  Scenario: Project GET a project information
    When I send a GET request to projects
    Then I expect the single response contains
  '''
  {"name": "(prefix)_project_(current_date_time)"}
  '''
    And I expect status code is 200

  Scenario: Project PUT new name
    When I send a PUT request to projects with data
  '''
  {"name": "(prefix)_new_name_(current_date_time)"}
  '''
    Then I expect the single response contains
  '''
  {"name": "(prefix)_new_name_(current_date_time)"}
  '''
    And I expect status code is 200


