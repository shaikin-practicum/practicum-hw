# Created by sergeishaikin at 03.05.2024
Feature: eBay Regression
  # Enter feature description here

  Scenario: Search bar verification
    Given Navigate to ebay
    And In search bar type "shoes"
    And Click "search" button
    Then All displayed items are relevant to keyword "shoes"
