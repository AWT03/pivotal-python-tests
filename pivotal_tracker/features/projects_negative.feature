Feature: projects
Background: precondition
  Given I start a connection with the Pivotal Tracker API
    And I log in as user member2
    And I send a POST request to projects with data
    '''
    {"name": "(prefix)_project_(current_date_time)"}
    '''
    And I send a DELETE request to projects

  Scenario: Project DELETE
     When I send a DELETE request to projects
     Then I expect status code is 403
      And I expect this error unauthorized_operation is thrown


  Scenario: Project PUT a new name
      When I send a PUT request to projects with data
          '''
          {"name": "(prefix)_new_name_(current_date_time)"}
          '''
      Then I expect status code is 403
       And I expect this error unauthorized_operation is thrown

  Scenario: Project GET a project information
     When I send a GET request to projects
     Then I expect status code is 403
      And I expect this error unauthorized_operation is thrown

  Scenario: Set the start date of a project with a distant past date
      When I send a PUT request to projects with data
          '''
          {"start_date": "1988-08-19"}
          '''
      Then I expect status code is 400
       And I expect this error too_far_in_the_past is thrown
