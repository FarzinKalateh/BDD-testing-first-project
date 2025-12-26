Feature: Login

  Scenario Outline: correct log in
    Given I open the browser
    And I open "https://ranobes.net/"
    When I try to log in with <userName> and <password>
    Then I should see myself logged in as <userName>

    Examples:
    |userName|password|
    |"1111"|"222222"|

  Scenario Outline: wrong capslock password log in
    Given I open the browser
    And I open "https://ranobes.net/"
    When I try to log in with <userName> and <wrong password>
    Then I should NOT see myself logged in as <userName>

    Examples:
    |userName|wrong password|
    |"1111"|"222222"|

  Scenario Outline: password with space log in
    Given I open the browser
    And I open "https://ranobes.net/"
    When I try to log in with <userName> and <wrong password>
    Then I should NOT see myself logged in as <userName>

    Examples:
    |userName|wrong password|
    |"1111"|"222222"|
    |"1111"|"222222"|
    |"1111"|"222222"|