Feature: Workspace

  Background: Preconditions
    Given I login the app as owner

  @gui @acceptance @clean_workspaces
  Scenario: Verify that I can create a Workspace
    When I go through ->Workspaces
    And I create a workspace with
      | key            | value                        |
      | workspace_name | (prefix)w(current_date_time) |
    Then I verify workspace_name is displayed on header_name
    And I go through WorkspaceMain->More
    And I verify that workspace settings were created according to characteristics
    And I verify workspace_name is displayed on header_name_more
    And I go through WorkspaceMain->Stories->SideBar
    And I verify that project counter is equal to 0
    And I go through ->WorkspaceSettings
    And I verify that workspace settings were created according to characteristics
    And I verify workspace_name is displayed on header_name_more
    And I go through Dashboard->Workspaces
    And I verify workspace_name is displayed on workspaces_list
    And I verify this message workspace_without_projects is displayed for this workspace_name
    And I do click on Workspace settings of the workspace_name
    And I verify that workspace settings were created according to characteristics
    And I click on Header Logo
    And I go through ->Workspaces
    And I verify workspace_name is displayed on workspaces_list
    And I do click on Workspace name of the workspace_name
    And I verify workspace_name is displayed on header_name
    And I do click on Main menu of the workspace_name
    And I verify workspace_name is displayed on workspaces_list
    And I click on Show All Workspaces
    And I verify workspace_name is displayed on workspaces_list
    And I verify that No projects is displayed for workspace_name
    And I verify 0 projects is displayed for workspace_name
    And I do click on Settings of the workspace_name
    And I verify that workspace settings were created according to characteristics
    And I go through AllWorkspaces
    And I do click on Workspace name of the workspace_name
    And I verify workspace_name is displayed on header_name
