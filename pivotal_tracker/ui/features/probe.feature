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
      And I click on More button
      And I fill the form with data
        | key          | value |
        | Enable Tasks | True  |
        | Save         | True  |
      And I click on Stories Tab button
      And I click on Add Story button
      And I fill the form with data
        | key         | value                              |
        | story_title | (prefix)_story_(current_date_time) |
      Then I verify that Task does not exist
      And I exist
