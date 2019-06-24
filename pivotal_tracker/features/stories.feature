Feature: stories
Background: precondition
  Given I start a connection with the API
    And I log in as user 1
    And I send a POST request to projects with data
    '''
    {"name": "(prefix)_project_(current_date_time)"}
    '''

#  Basic operations
  Scenario: Story POST
     When I send a POST request to stories with data
    '''
    {"name": "(prefix)_story_(current_date_time)"}
    '''
     Then I expect status code is 200
      And I expect the single response contains
      '''
      {"name": "(prefix)_story_(current_date_time)"}
      '''
	  And I expect the response id is not null

  Scenario: Story DELETE
     When I send a POST request to stories with data
          '''
          {"name": "(prefix)_story_(current_date_time)"}
          '''
      And I send a DELETE request to stories
     Then I expect status code is 204

  Scenario: Stories PUT a new name
     When I send a POST request to stories with data
          '''
          {"name": "(prefix)_story_(current_date_time)"}
          '''
      And I send a PUT request to stories with data
          '''
          {"name": "(prefix)_new_name_(current_date_time)"}
          '''
     Then I expect the single response contains
          '''
          {"name": "(prefix)_new_name_(current_date_time)"}
          '''
      And I expect status code is 200

  Scenario: Story GET a story information
     When I send a POST request to stories with data
          '''
          {"name": "(prefix)_story_(current_date_time)"}
          '''
      And I send a GET request to stories
     Then I expect the single response contains
          '''
          {"name": "(prefix)_story_(current_date_time)"}
          '''
      And I expect status code is 200

  Scenario: Story GET all stories in project
     When I send a GET request to stories
     Then I expect the response is a list
      And I expect status code is 200
