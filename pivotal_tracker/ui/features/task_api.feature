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
      And I send a POST request to stories with data
    '''
    {"name": "(prefix)_story_(current_date_time)"}
    '''
    And I save story_name


  Scenario: Verify that new a task is creates
    When  I login the app as owner
      And I go to Dashboard->Projects
      #And I access_project that contains project_name saved
    #I open the "project_name" project
      And I go to ProjectMain->Stories
      #And I access_story that contains story_name saved
    #I expand the "story_name" story
      And I create a story with
      | key         | value                              |
      | story_title | (prefix)_story_(current_date_time) |


    #With separate steps; every access, open, is a separate step.