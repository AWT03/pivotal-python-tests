Feature: Create Task

  Background: Preconditions
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with data
  '''
  {
  "name": "(prefix)_project_(current_date_time)",
  "account_id": "(current_account_id)"
  }
  '''
    And I send a GET request to projects
    And I send a POST request to stories with data
  '''
  {
  "name": "(prefix)_story_(current_date_time)"
  }
  '''
    And I send a GET request to story
    And I send a POST request to tasks with data
  '''
  {
  "description": "(prefix)_task_(current_date_time)",
  "complete": "false",
  "position": "1"
  }
  '''
    And I send a GET request to tasks
    And I login the app as owner
    And I click on Link element of the Project Name on Dashboard panel
    And I click on Arrow element of the Story Name on Icebox panel

  @gui @task @acceptance @clean_response
  Scenario: Verify that I can delete a Task on Icebox panel
    When I mouse hover the Task Description create before
    And I click on Delete button
    Then I verify that task description is not displayed in the panel
    And I verify that 1 is subtracted to the task counter

  @gui @task @acceptance @clean_response
  Scenario: Verify that I can update a Task on Icebox panel
    When I click on Task Description element
    And I fill the form with data to update
      | key         | value                                 |
      | description | (prefix)_new_task_(current_date_time) |
    And I click on Save button
    Then I verify that Task description is displayed in the panel
