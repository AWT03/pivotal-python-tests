Feature: Projects

  Background: Preconditions
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with data
      '''
      {
      "name": "(prefix)_project_(current_date_time)"
      }
      '''

  @acceptance
  Scenario: Verify that I can delete a specific Project
    When I send a DELETE request to projects
    Then I expect status code is 204
    And I send a GET request to projects
    And I expect this error unauthorized_operation is thrown



#Feature: Create stories
#  Background: preconditions
#    Given I start a connection with the Pivotal Tracker API
#    And I log in as user owner
#    And I send a POST request to projects with data
#    '''
#    {
#    "name": "(prefix)_project_(current_date_time)"
#    }
#    '''
##    And I save project name
#
#  Scenario: Verify
#    When I save project name

#  Scenario: Verify that new a story is create with correct type
#    Scenario Outline: Verify that I can create projects with different project_type
#      When I send a POST request to story with data
#        | name   | story_type   |
#        | <name> | <story_type> |
#    Then I expect status code is 200
#      And I login the app as owner
#      And I go to AllProjects
#      And I verify project_name is displayed on projects_list
#      And I click on <name>
#      And I click on expand_story
#      And I verify feature is displayed on story_type
#    Examples:
#      | name                    | story_type |
#      | (prefix)_story_(random) | feature    |
#      | (prefix)_story_(random) | bug        |
#      | (prefix)_story_(random) | chore      |
#      | (prefix)_story_(random) | release    |
      
    



#    Scenario: verify that
#    When I create a project with
#        | key           | value                                |
#        | project_name  | (prefix)_project_(current_date_time) |
#        | account       | (prefix)_account                     |
#        | privacy       | public                               |
#    Then I verify project_name is displayed on header_name
#    And I go to ProjectMain->More
#    And I modify project settings with
#      | key          | value |
#      | enable_tasks | false |
#    And I go to ProjectMain->Stories
#    And I create a story with
#      | key         | value                              |
#      | story_title | (prefix)_story_(current_date_time) |
