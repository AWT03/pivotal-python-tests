Feature: projects

  Background: common log in
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner

  Scenario Outline: Create a project with out of wrong iteration length
    When I send a POST request to projects with data
      | name   | iteration_length   |
      | <name> | <iteration_length> |
    Then I expect status code is 400
    And I expect this error <error> is thrown
    Examples:
      | name                      | iteration_length | error                               |
      | (prefix)_project_(random) | -1               | iteration_length_out_of_range       |
      | (prefix)_project_(random) | 8                | iteration_length_out_of_range       |
      | (prefix)_project_(random) | 1.2              | iteration_length_only_integer_value |
      | (prefix)_project_(random) | hello            | iteration_length_only_integer_value |

  Scenario Outline: Create a project with different project_type
    When I send a POST request to projects with data
      | name   | week_start_day   | start_date   |
      | <name> | <week_start_day> | <start_date> |
    Then I expect status code is 400
    Examples:
      | name                      | week_start_day | start_date |
      | (prefix)_project_(random) | Monday         | 2019-07-16 |
      | (prefix)_project_(random) | Tuesday        | 2019-07-17 |
      | (prefix)_project_(random) | Wednesday      | 2019-07-18 |
      | (prefix)_project_(random) | Thursday       | 2019-07-19 |
      | (prefix)_project_(random) | Friday         | 2019-07-20 |


  Scenario: POST a project with "public" attribute as "false" and prohibit other accounts to see projects information
    When I send a POST request to projects with data
  '''
  {"name": "(prefix)_project_(current_date_time)",
  "public": "false"}
  '''
    And I log in as user member1
    And I send a GET request to projects
    Then I expect status code is 403

  Scenario: Set the start date of a project with a distant past date
    When I send a POST request to projects with data
  '''
  {"start_date": "1988-08-19"}
  '''
    Then I expect status code is 400
    And I expect this error too_far_in_the_past is thrown
