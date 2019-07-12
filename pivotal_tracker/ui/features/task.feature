Feature: Create projects
  Background: preconditions
    Given I login the app as owner

  @gui
  Scenario: Verify that I can create a new Project
     When I click on Create Project button
      And I fill the form with data
        | key           | value                                |
        | project_name  | (prefix)_project_(current_date_time) |
        | account       | (prefix)_account                     |
        | private       | True                                 |
        | public        | False                                |
      And I click on Create button
      And I click on Add Story button
      And I fill the form with data
        | key         | value                              |
        | story_title | (prefix)_story_(current_date_time) |
      And I click on Add a task button
      And I click on Save button
      And I fill the form with data
        | key       | value                             |
        | task_name | (prefix)_task_(current_date_time) |
      And I click on Add button
      Then I exist


