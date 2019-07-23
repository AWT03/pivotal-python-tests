Feature: Workspace

  Background: Preconditions
    Given I login the app as owner

  @gui @acceptance
  Scenario: Verify that I can create a Workspace
#    When I go to Workspaces
#    And I click on Create workspace
    When I go to ->Workspaces
#    When I click on Workspaces
    And I create a workspace with
      | key            | value                        |
      | workspace_name | (prefix)w(current_date_time) |
#    And I click on Create
    Then I verify workspace_name is displayed on header_name
