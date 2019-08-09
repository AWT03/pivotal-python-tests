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

    Scenario: Verify that I can create story
    When  I login the app as owner
      And I go to Dashboard->Projects
      And I access_project that contains project_name saved
      And I go to ProjectMain->Stories
      And I create a story with
        | key         | value                              |
        | story_title | (prefix)_story_(current_date_time) |
        | task_title  | (prefix)_task_(current_date_time)  |
        | label       | (prefix)_label_                    |
        | comment     | (prefix)_comment                   |
