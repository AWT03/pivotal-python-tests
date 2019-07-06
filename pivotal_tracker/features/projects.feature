@wip
Feature: projects
Background: common log in
  Given I start a connection with the API
    And I log in as user 1

  Scenario: Project POST
     When I send a POST request to projects with data
          '''
          {"name": "(prefix)_project_(current_date_time)"}
          '''
     Then I expect status code is 200
      And I expect the single response contains
          '''
          {"name": "(prefix)_project_(current_date_time)"}
          '''
	  And I expect the response id is not null

  Scenario: Project DELETE
     When I send a POST request to projects with data
          '''
          {"name": "(prefix)_project_(current_date_time)"}
          '''
      And I send a DELETE request to projects
     Then I expect status code is 204

  Scenario: Project PUT a new name
     When I send a POST request to projects with data
          '''
          {"name": "(prefix)_project_(current_date_time)"}
          '''
      And I send a PUT request to projects with data
          '''
          {"name": "(prefix)_new_name_(current_date_time)"}
          '''
     Then I expect the single response contains
          '''
          {"name": "(prefix)_new_name_(current_date_time)"}
          '''
      And I expect status code is 200

  Scenario: Project GET a project information
     When I send a POST request to projects with data
          '''
          {"name": "(prefix)_project_(current_date_time)"}
          '''
      And I send a GET request to projects
     Then I expect the single response contains
          '''
          {"name": "(prefix)_project_(current_date_time)"}
          '''
      And I expect status code is 200

  Scenario: Project GET all projects information
      When I send a GET request to projects
     Then I expect the response is a list
      And I expect status code is 200

# Hooks after and before scenario, they are run on every scenario
# Hooks with tag on a specific scenario
# Hook before all - delete/disable/hide all objects with prefix
# Hook after - delete/disable/hide objects created
# Acceptance, Functional
# Negative (if i don't send something what error messages we get)
# Corner test cases, is validating data is logically correct/coherent