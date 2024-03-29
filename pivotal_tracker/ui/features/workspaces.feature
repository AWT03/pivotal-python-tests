Feature: Workspace

  Background: Preconditions
    Given I login the Pivotal Tracker web application as owner

  @gui @acceptance @clean_workspaces
  Scenario: Verify that I can create a Workspace
    When I go to ->Workspaces
    And I create a workspace with
      | key            | value                        |
      | workspace_name | (prefix)w(current_date_time) |
    Then I verify workspace_name is displayed on header_name
    And I verify that project_counter is displayed as 0
    And I go to WorkspaceMain->More
    And I verify that workspace settings were created according to characteristics
    And I verify workspace_name is displayed on header_name_more
    And I go to Dashboard->Workspaces
    And I verify workspace_name is displayed on workspaces_list
    And I do click on Workspace name of the workspace_name
    And I go to MainMenu
    And I verify workspace_name is displayed on workspaces_list
    And I click on Show All Workspaces
    And I verify workspace_name is displayed on workspaces_list
    And I verify that "No projects" is displayed for workspace_name
    And I verify 0 projects is displayed for workspace_name
    And I go to MainMenu
    And I click on Show All Workspaces
    And I do click on Workspace name of the workspace_name
    And I verify workspace_name is displayed on header_name
