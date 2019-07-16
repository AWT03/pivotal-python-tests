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
    And I login the app as owner
    And I open the Project Name on Dashboard
    And I open the Story Name on Icebox

  @gui @task @acceptance @clean_response
  Scenario: Verify that I can create a new Task on Icebox panel
    When I click on Add a task button
    And I fill the form with data to create
      | key         | value                             |
      | description | (prefix)_task_(current_date_time) |
    And I click on Add button
    Then I verify that "Task" "description" is "displayed"
    And I verify that task counter is "incremented" by "1"
