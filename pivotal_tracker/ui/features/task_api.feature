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
      And I send a POST request to stories with data
    '''
    {"name": "(prefix)_story_(current_date_time)"}
    '''

  Scenario: Verify
    When I save project name

  Scenario: Verify that new a story is create with correct type
      When I send a POST request to story with data
        | name   | story_type   |
        | <name> | <story_type> |
    Then I expect status code is 200
      And I login the app as owner
      And I go to AllProjects
      And I verify project_name is displayed on projects_list
      And I click on project_name
      And I click on expand_story
          And I create a story with
      | key         | value                              |
      | story_title | (prefix)_story_(current_date_time) |
      | task_title  | (prefix)_task_(current_date_time)  |
