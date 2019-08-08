Feature: Update a Workspace
  As a user,
  I want to update a Workspace,
  so I can not use outdated information.

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


  @gui @acceptance @clean_workspaces
  Scenario: Verify that I can update to a Workspace from more page
    Given I go to Dashboard->Workspaces
    And I open the Workspace Name
    When I go to WorkspaceMain->More
    And I update a workspace with
      | key            | value                        |
      | workspace_name | (prefix)W(current_date_time) |
    Then I verify that "changes_saved" message is displayed
    And I go to Dashboard->Workspaces
    And I verify workspace_name is displayed on workspaces_list


  @gui @acceptance @clean_workspaces
  Scenario: Verify that I can update to a Workspace from settings
    Given I go to Dashboard->Workspaces
    When I do click on Workspace settings of the workspace_name
    #This action should be done on previous click
    And I go to WorkspaceMain->More
    And I update a workspace with2
      | key            | value                        |
      | workspace_name | (prefix)W(current_date_time) |
    Then I verify that "changes_saved" message is displayed
    And I go to MainMenu
    And I click on Show All Workspaces
    And I verify workspace_name is displayed on workspaces_list


  @gui @acceptance @clean_workspaces
  Scenario: Verify that I can update to a Workspace from story side bar settings
    Given I go to Dashboard->Workspaces
    And I open the Workspace Name
    When I open the workspace settings from stories
    #This action should be done on previous click
    And I go to WorkspaceMain->More
    And I update a workspace with2
      | key            | value                        |
      | workspace_name | (prefix)W(current_date_time) |
    Then I verify that "changes_saved" message is displayed
    And I go to MainMenu
    And I click on Show All Workspaces
    And I verify workspace_name is displayed on workspaces_list


  @gui @acceptance @clean_workspaces
  Scenario: Verify that I can update to a Workspace from the Show All Workspace List
    Given I go to MainMenu
    And I click on Show All Workspaces
    When I do click on Settings of the workspace_name
    #This action should be done on previous click
    And I go to WorkspaceMain->More
    And I update a workspace with
      | key            | value                        |
      | workspace_name | (prefix)W(current_date_time) |
    Then I verify that "changes_saved" message is displayed
    And I go to MainMenu
    And I click on Show All Workspaces
    And I verify workspace_name is displayed on workspaces_list
