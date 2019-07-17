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
    And I open the Project Name on Dashboard
    And I open the Story Name on Icebox

  @gui @task @acceptance @clean_response @clean_projects
  Scenario: Verify that I can delete a Task on Icebox panel
    When I Delete the Task Description
    Then I verify that "Task" "description" is "not displayed"
    And I verify that task counter is "decremented" by "1"

  @gui @task @acceptance @clean_response @clean_projects @wip
  Scenario: Verify that I can update a Task on Icebox panel
    When I click on Task Description element
    And I fill the form with data to update
      | key         | value                                 |
      | description | (prefix)_new_task_(current_date_time) |
    And I click on Save button
    Then I verify that "Task" "description" is "displayed"
