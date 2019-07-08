# On this feature we will make sure all functions are working
Feature: Story features as a single object

# We define a background that will be run each scenario
# For each case we need a project and a story to interact with
Background: preconditions
  Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with data from stories/project.json
    And I send a POST request to story with data from stories/base.json

  # We delete the initial post to check if delete option is working
  Scenario: Verify that I can delete a Story
     When I send a DELETE request to story
     Then I expect status code is 204
     When I send a GET request to story
     Then I expect status code is 404
      And I expect the error message unfound_resource

  # We put an arbitrary new name to the already created story
  Scenario: Verify that I can change a Story's name
     When I send a PUT request to story with data from stories/put_name.json
     Then I expect the single response contains data from stories/put_name.json
      And I expect status code is 200

  # We get the information from the created story
  Scenario: Verify that I can get a specific Story information
     When I send a GET request to story
     Then I expect the single response contains data from stories/base.json
      And I expect status code is 200
