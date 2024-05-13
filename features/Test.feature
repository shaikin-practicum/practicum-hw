# Created by sergeishaikin at 03.05.2024
Feature: eBay Regression
  # Enter feature description here

  Scenario: Search bar verification
    Given Navigate to ebay
    And In search bar type "shoes"
    And Click "search" button
    Then All displayed items are relevant to span and role and 'heading' and text() and 'Shoes'

  Scenario: "Daily Deals" verification
    Given Navigate to ebay
    And Click 'Daily Deals' link
    Then All displayed items are relevant to span and class and 'itemtile-price-bold' and text() and 'off'

  Scenario: "Brand Outlet" verification
    Given Navigate to ebay
    And Click 'Brand Outlet' link
    Then All displayed items are relevant to div and class and 'b-visualnav__title' and text() and 'brand'

  Scenario: "Gift Cards" verification
    Given Navigate to ebay
    And Click 'Gift Cards' link
    Then All displayed items are relevant to a and id and 'birthday' and @class and 'card'
