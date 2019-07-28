Feature: Workspace

  Background: Preconditions
    Given I login the app as owner
    And I go to ->Workspaces
    And I create a workspace with
      | key            | value                        |
      | workspace_name | (prefix)w(current_date_time) |

  @gui @acceptance @clean_workspaces
  Scenario: Verify that I can delete a Workspace
    When I go to WorkspaceMain->More
    And I click on Delete
    Then I verify that "success_delete" message is displayed for "workspace_name"
    And I go to ->Workspaces
    And I verify workspace_name is not displayed on workspaces_list
