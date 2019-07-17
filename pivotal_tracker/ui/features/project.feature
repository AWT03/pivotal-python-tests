Feature: Create projects
  Background: preconditions
    Given I login the app as owner

  @gui @clean_projects
  Scenario: Verify that I can create a new Project
     When I click on Create Project button
      And I fill the form with data
        | key           | value                                |
        | project_name  | (prefix)_project_(current_date_time) |
        | account       | (prefix)_account                     |
        | private       | True                                 |
        | public        | False                                |
      And I click on Create button
     Then I click on More button
