Feature: Project
Background: precondition
  Given I start a connection with the Pivotal Tracker API
    And I log in as user member2
    And I send a POST request to projects with data
    '''
    {"name": "(prefix)_project_(current_date_time)"}
    '''
    And I send a POST request to stories with data
    '''
    {"name": "(prefix)_story_(current_date_time)"}
    '''

  Scenario: Project enable to create tasks
     When I send a PUT request to projects with data
      '''
        {"enable_tasks": "true"}
      '''
     And I send a POST request to tasks with data
    '''
    {"description": "(prefix)_task_(current_date_time)"}
    '''
     Then I expect status code is 200

  Scenario: Project disable to create tasks
     When I send a PUT request to projects with data
      '''
      {"enable_tasks": "false"}
      '''
     And I send a POST request to tasks with data
    '''
    {"description": "(prefix)_task_(current_date_time)"}
    '''
     Then I expect status code is 200

