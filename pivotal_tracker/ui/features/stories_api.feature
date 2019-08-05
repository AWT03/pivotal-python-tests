Feature: Create stories
  Background: preconditions
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with data
    '''
    {
    "name": "(prefix)_project_(current_date_time)"
    }
    '''
    And I save project_name

      @acceptance
  Scenario: Verify that I can get a project information
    When
    When  I login the app as owner
      And I click on project_name created by API
      And I create a story with
      | key         | value                              |
      | story_title | (prefix)_story_(current_date_time) |
