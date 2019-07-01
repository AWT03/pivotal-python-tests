# On this feature we will make sure all functions are working
Feature: Story Functions

# We define a background that will be run each scenario
# For each case we need a project and a story to interact with
Background: precondition
  Given I start a connection with the API
    And I log in as user owner
    And I send a POST request to projects with data
    '''
    {"name": "(prefix)_project_(current_date_time)",
     "account_id": "(current_account_id)"}
    '''
    And I send a POST request to story with data
    '''
    {"name": "(prefix)_story_(current_date_time)"}
    '''

  # We delete the initial post to check if delete option is working
  Scenario: Story DELETE
     When I send a DELETE request to story
     Then I expect status code is 204
     When I send a GET request to story
     Then I expect status code is 404
      And I expect the single response contains
          '''
          {"code": "unfound_resource"}
          '''

  # We put an arbitrary new name to the already created story
  Scenario: Stories PUT a new name
     When I send a PUT request to story with data
          '''
          {"name": "(prefix)_new_name_(current_date_time)"}
          '''
     Then I expect the single response contains
          '''
          {"name": "(prefix)_new_name_(current_date_time)"}
          '''
      And I expect status code is 200

  # We get the information from the created story
  Scenario: Story GET a story information
     When I send a GET request to story
     Then I expect the single response contains
          '''
          {"name": "(prefix)_story_(current_date_time)"}
          '''
      And I expect status code is 200
