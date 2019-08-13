Feature: Create stories
  Background: preconditions
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with data
      | name                                |
      | (prefix)_multiple_projects_(random) |
    And I save project_name
    And I login the Pivotal Tracker web application as owner

    @wisp
    Scenario: Verify that I can create a story
      When I go to Dashboard->Projects
      And I open the project_name project
      And I go to ProjectMain->Stories
      When I create a story with
        | key         | value                                    |
        | story_title | (prefix)_story_(current_date_time)       |
        | task_title  | (prefix)_task_(current_date_time)        |
        | comment     | (prefix)_comment_(current_date_time)     |
        | description | (prefix)_description_(current_date_time) |
      And I expand the story_title story
      Then I verify story_title is displayed on title_box
      And I verify task_title is displayed on task_list
      And I verify description is displayed on description_box
      And I verify comment is displayed on activity_list









