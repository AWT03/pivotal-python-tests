Feature: Workspace

  Background: Preconditions
    Given I login the app as owner

  @gui @acceptance
  Scenario: Verify that I can create a Workspace
    When I go to ->Workspaces
    And I create a workspace with
      | key            | value                        |
      | workspace_name | (prefix)w(current_date_time) |
    Then I verify workspace_name is displayed on header_name
    And I go to WorkspaceMain->More
    And I verify workspace settings were created according to characteristics
    And I verify workspace_name is displayed on header_name_more
    And I go to WorkspaceMain->Stories->LeftPanel
    And I verify that project counter is equal to 0
    And I go to ->WorkspaceSettings
    And I verify workspace settings were created according to characteristics
    And I verify workspace_name is displayed on header_name_more
#    And I go to WorkspaceMain->Dashboards
#    And I go to ->Workspaces
#    And I verify workspace settings were created according to characteristics
#    And I click on WorkspaceSetting
#    And I verify workspace settings were created according to characteristics
#    And I click on MainMenu
#    And I verify workspace_name is displayed on the list

