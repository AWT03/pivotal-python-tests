Feature: Create stories
  Background: preconditions
    Given I login the app as owner

  Scenario: Verify that new stories are created in a story
    When I create a project with
        | key           | value                                |
        | project_name  | (prefix)_project_(current_date_time) |
        | account       | (prefix)_account                     |
        | privacy       | public                               |
    Then I verify project_name is displayed on header_name
    And I go to ProjectMain->Stories
    And I create a story with
      | key         | value                              |
      | story_title | (prefix)_story_(current_date_time) |

    #


