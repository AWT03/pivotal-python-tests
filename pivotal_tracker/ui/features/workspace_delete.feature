Feature: Delete a Workspace
  As a Owner user,
  I want to delete a Workspace,
  so I can not have old Workspaces.

  Background: Preconditions
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to workspaces with data
  '''
  {
  "name": "(prefix)w(current_date_time)"
  }
  '''
    And I login the Pivotal Tracker web application as owner


  @gui @acceptance @clean_workspaces @wip
  Scenario: Verify that I can delete a Workspace from more page
    Given I go to Dashboard->Workspaces
    When I open the Workspace Name
    And I go to WorkspaceMain->More
    And I click on Delete
    Then I verify that "success_delete" message is displayed for "workspace_name"
    And I go to ->Workspaces
    And I verify workspace_name is not displayed on workspaces_list


  @gui @acceptance @clean_workspaces @wip
  Scenario: Verify that I can delete to a Workspace from settings
    Given I go to Dashboard->Workspaces
    When I do click on Workspace settings of the workspace_name
    #This action should be done on previous click
    And I go to WorkspaceMain->More
    And I click on Delete
    Then I verify that "success_delete" message is displayed for "workspace_name"
    And I go to ->Workspaces
    And I verify workspace_name is not displayed on workspaces_list


  @gui @acceptance @clean_workspaces @wip
  Scenario: Verify that I can delete to a Workspace from story side bar settings
    Given I go to Dashboard->Workspaces
    And I open the Workspace Name
    When I open the workspace settings from stories
    And I click on Delete
    Then I verify that "success_delete" message is displayed for "workspace_name"
    And I go to ->Workspaces
    And I verify workspace_name is not displayed on workspaces_list


  @gui @acceptance @clean_workspaces @wip
  Scenario: Verify that I can delete to a Workspace from the Show All Workspace List
    Given I go to MainMenu
    And I click on Show All Workspaces
    When I do click over Workspace settings of the workspace_name
    #This action should be done on previous click
    And I go to WorkspaceMain->More
    And I do click on Delete button
    Then I verify that "success_delete" message is displayed for "workspace_name"
    And I go to ->Workspaces
    And I verify workspace_name is not displayed on workspaces_list
