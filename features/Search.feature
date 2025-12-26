Feature: search feature

  Scenario Outline: search for complete name with respect to capslock
    Given I open the browser
    And I open "https://ranobes.net/search/"
    When I type <Novel Name> in the search box
    Then I should see <Novel Name> as one of search results

    Examples:
    |Novel Name|
    |"Mother of Learning"|
    |"The Perfect Run"   |


  Scenario Outline: search for complete name without respecting capslock
    Given I open the browser
    And I open "https://ranobes.net/search/"
    When I type <name without capslock> in the search box
    Then I should see <NovelName> as one of search results

    Examples:
    |name without capslock|NovelName|
    |"mother of learning" |"Mother of Learning"|
    |"the perfect run"    |"The Perfect Run"   |
    |"shadow slave"       |"Shadow Slave"      |


  Scenario Outline: search for complete name without respecting capslock
    Given I open the browser
    And I open "https://ranobes.net/search/"
    When I type <name without capslock> in the search box
    Then I should see <NovelName> as one of search results

    Examples:
    |name without capslock|NovelName|
    |"MotherOfLearning" |"Mother of Learning"|
    |"ThePerfectRun"    |"The Perfect Run"   |


  Scenario Outline: search for complete name with extra space in the name
    Given I open the browser
    And I open "https://ranobes.net/search/"
    When I type <name without capslock> in the search box
    Then I should see <NovelName> as one of search results

    Examples:
    |name without capslock|NovelName|
    |"Mother Of  Learning" |"Mother of Learning"|
    |" The Perfect Run"    |"The Perfect Run"   |

