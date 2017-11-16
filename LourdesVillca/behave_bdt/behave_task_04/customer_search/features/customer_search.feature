Feature: customer search

  Scenario Outline: Search a total priced for a list of clients
    Given I send the client name <ClientName> to make a Search
    And  I send the the Client ID <Id>
    When I press the "Search" option
    Then I should see the total purchase price <Price>
    Examples:
      | ClientName | Id   | Price  |
      | Lourdes    | 1001 | 45.6   |
      | Alvaro     | 1002 | 1300   |
      | Juana      | 1003 | 550.67 |