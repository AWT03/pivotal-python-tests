Feature: Create stories
  Background: preconditions
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    When I send a POST request to projects with data
      | name                                |
      | (prefix)_multiple_projects_(random) |
    And I save project_name

    Scenario: Verify that stories are created and registered when completed
    When I login the app as owner
    And I go to Dashboard->Projects
    And I open the project_name project
    And I go to ProjectMain->Stories
      When I create a story with
        | key         | value                              |
        | story_title | (prefix)_story_(current_date_time) |
        | task_title  | (prefix)_task_(current_date_time)  |
      And I expand the story_title story
      Then I verify task_title is displayed on task_list
      And I verify 0/1 is displayed on task_counter
      And Check task_title box as completed
      And I verify 1/1 is displayed on task_counter




