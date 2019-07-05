Feature: projects
Background: common log in
    Given I start a connection with the Pivotal Tracker API
    And I log in as user member2


    Scenario: Project name is larger than 50 characters
    When I send a POST request to projects with data from project.json
     Then I expect status code is 400
     And I expect this error too_large_name is thrown
