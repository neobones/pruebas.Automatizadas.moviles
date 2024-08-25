Feature: User Login

  Scenario: Successful login with valid credentials
    Given the app is launched
    When I enter username "user@example.com"
    And I enter password "password123"
    And I tap the login button
    Then I should see the home screen