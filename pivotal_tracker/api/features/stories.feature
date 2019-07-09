# On this feature we will make sure all functions are working
Feature: Stories features as a whole

# We define a background that will be run each scenario
# For each case we need a project to interact with
  Background: precondition
    Given I start a connection with the Pivotal Tracker API
    And I log in as user owner
    And I send a POST request to projects with data from stories/project.json

  # We can post a story on the project
  @functional
  Scenario: Verify that I can create a Story with default values
    When I send a POST request to stories with data from stories/base.json
    Then I expect status code is 200
    And I expect the single response contains data from stories/base.json
    And I expect the response id is not null

  # Default values can be changed at the moment of creation
  @functional
  Scenario: Verify that params can be set while creating a Story
    When I send a POST request to stories with data from stories/complete.json
    Then I expect status code is 200
    And I expect the single response contains data from stories/complete_validation.json
    And I expect the response id is not null

  # We get the information of all stories in the project
  @functional
  Scenario: Verify that I can get the information from all my stories
    When I send a POST request to stories with data from stories/base.json
    And I send a GET request to stories
    Then I expect the response list contains 1 values
    And I expect status code is 200

  # Other objects can be created while posting a new story
  @acceptance
  Scenario Outline: Verify that other objects can be created through Story POST
    When I send a POST request to stories with data from stories/<archive_id>.json
    Then I expect status code is 200
    And I expect the response id is not null
    And I save the response id as URL reference
    And I send a GET request to <object_reference>
    And I expect the response list contains <n_values> values
    Examples:
      | archive_id | object_reference | n_values |
      | tasks      | tasks            | 2        |
      | comments   | comments         | 3        |
      | blockers   | blockers         | 2        |

  # Domain testing for variable "created at" valid domain
  @corner_cases
  Scenario Outline: Verify "created at" variable valid domain on primary dimensions
    When I send a POST request to stories with data from stories/domain/<archive_id>.json
    Then I expect status code is 200
    And I expect the single response contains data from stories/domain/<archive_id>.json
    Examples:
      | archive_id        |
      | top_created_at    |
      | bottom_created_at |

#  Domain testing for variable "created at" outside valid domain
  @corner_cases
  Scenario Outline: Verify "created at" variable invalid domain on primary dimensions
    When I send a POST request to stories with data from stories/domain/<archive_id>.json
    Then I expect status code is 400
    And I expect the error message invalid_parameter
    Examples:
      | archive_id      |
      | low_created_at  |
      | high_created_at |

