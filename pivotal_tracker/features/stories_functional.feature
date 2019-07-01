# On this feature we will make sure all functions are working
Feature: Stories Functions

# We define a background that will be run each scenario
# For each case we need a project to interact with
Background: precondition
  Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with project data from /pivotal_tracker/features/test_data/stories.json

  # We can post a story on the project
  Scenario: Story POST
     When I send a POST request to stories with base data from /pivotal_tracker/features/test_data/stories.json
     Then I expect status code is 200
      And I expect the single response contains base data from /pivotal_tracker/features/test_data/stories.json
	  And I expect the response id is not null

  # We get the information of all stories in the project
  Scenario: Story GET all stories in project
     When I send a POST request to stories with base data from /pivotal_tracker/features/test_data/stories.json
      And I send a GET request to stories
     Then I expect the response list contains 1 values
      And I expect status code is 200
