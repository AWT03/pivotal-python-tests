Feature: Create stories
  Background: preconditions
    Given I login the app as owner

    Scenario: Verify that fields of the story are available
    When I create a project with
        | key           | value                                |
        | project_name  | (prefix)_project_(current_date_time) |
        | account       | (prefix)_account                     |
        | privacy       | public                               |
    Then I verify project_name is displayed on header_name
    And I go to ProjectMain->More
    And I modify project settings with
      | key          | value |
      | enable_tasks | true |
    And I go to ProjectMain->Stories
    And I create a story with
      | key         | value                              |
      | story_title | (prefix)_story_(current_date_time) |
      | task_title  | (prefix)_task_(current_date_time)  |
      | label       | (prefix)_label_(current_date_time) |
      | description | (prefix)_description               |
      | activity    | (prefix)_activity                  |
    And I click on expand?button
    And I verify story_title is displayed on title_box
    And I verify task_title is displayed on task_list
    And I verify label is displayed on label_list
    And I verify description is displayed on description_bos
    And I verify activity is displayed on  activity_list



