# Created by sergeishaikin at 03.05.2024
Feature: eBay Regression
  # Enter feature description here

  Scenario: Search bar verification
    Given Navigate to ebay
    And In search bar type "shoes"
    And Click "search" button
    Then All displayed items are relevant to keyword "shoes"

  Scenario: "Daily Deals" verification
    Given Navigate to ebay
    And Click 'Daily Deal' link
    Then All displayed items are relevant to "Daily Deals"

  Scenario: "Brand Outlet" verification
    Given Navigate to ebay
    And Click 'Brand Outlet' link
    Then All displayed items are relevant to "Brand Outlet"
