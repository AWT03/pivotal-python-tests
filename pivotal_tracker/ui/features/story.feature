Feature: Create stories
  Background: preconditions
    Given I login the app as owner
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
        | label       | (prefix)_label_(current_date_time) |
        | label       | (prefix)_label_                    |
        | comment     | (prefix)_comment                   |
      And I expand the (prefix)_story_(current_date_time) story
      Then I verify story_title is displayed on title_box
      And I verify task_title is displayed on task_list
      And I verify label is displayed on label_list
      And I verify description is displayed on description_bos
      And I verify comment is displayed on  activity_list




