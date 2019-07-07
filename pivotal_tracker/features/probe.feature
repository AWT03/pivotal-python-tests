Feature: projects
Background: common log in
    Given I start a connection with the Pivotal Tracker API
    And I log in as user member2


  Scenario: Task GET all tasks in story
    Given I send a POST request to projects with data
      | name                   |
      | (prefix)_multiple_projects_(random) |
      | (prefix)_multiple_projects_(random) |
      | (prefix)_multiple_projects_(random) |
    When I send a GET request to projects
    Then I expect status code is 200
    And I expect the response list contains 3 values
    And I expect the items' ids obtained are equal to the items' ids created before
    And I expect the items' value obtained are equal to the items' value created before
