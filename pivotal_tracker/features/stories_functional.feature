# On this feature we will make sure all functions are working
Feature: Stories Functions

# We define a background that will be run each scenario
# For each case we need a project and a story to interact with
Background: precondition
  Given I start a connection with the API
    And I log in as user 3190382
    And I send a POST request to projects with data
    '''
    {"name": "(prefix)_project_(current_date_time)",
     "account_id": "(current_account_id)"}
    '''
   When I send a POST request to stories with data
    '''
    {"name": "(prefix)_story_(current_date_time)"}
    '''

  # Since there is always a post to stories, we just check that POST is done
  Scenario: Story POST
     Then I expect status code is 200
      And I expect the single response contains
      '''
      {"name": "(prefix)_story_(current_date_time)"}
      '''
	  And I expect the response id is not null

  # We delete the initial post to check if delete option is working
  Scenario: Story DELETE
     When I send a DELETE request to stories
     Then I expect status code is 204

  # We put an arbitrary new name to the already created story
  Scenario: Stories PUT a new name
     When I send a PUT request to stories with data
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
     When I send a GET request to stories
     Then I expect the single response contains
          '''
          {"name": "(prefix)_story_(current_date_time)"}
          '''
      And I expect status code is 200

  # We get the information of all stories in the project
  Scenario: Story GET all stories in project
     When I make sure last id is None
      And I send a GET request to stories
     Then I expect the response is a list
      And I expect status code is 200
