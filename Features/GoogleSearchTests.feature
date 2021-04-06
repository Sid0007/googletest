# Created by Narla at 06/04/2021
Feature: Google Search Test
  # Enter feature description here

  Scenario: Test google search
    Given I am on google search page
    When I type in text to search
    And I hit search button
    Then I should be on the search result page

