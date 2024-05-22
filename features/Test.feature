# Created by sergeishaikin at 03.05.2024
Feature: eBay Regression
  # Enter feature description here

  Scenario: Search bar verification
    Given Navigate to ebay
    And In search bar type "shoes"
    And Click "search" button
    Then All displayed items are relevant to 'heading' and 'Shoes'

  Scenario: "Daily Deals" verification
    Given Navigate to ebay
    And Click 'Daily Deal' link
    Then All displayed items are relevant to 'itemtile-price-bold' and 'off'

  Scenario: "Brand Outlet" verification
    Given Navigate to ebay
    And Click 'Brand Outlet' link
    Then All displayed items are relevant to 'b-visualnav__title' and 'brand'

  Scenario:  "Gift Cards" verification
    Given Navigate to ebay
    And Click 'Gift Cards' link
    Then All displayed items are relevant to 'item-card__title' and 'Birthday'

  Scenario: Filter validation
    Given Navigate to ebay
    And In search bar type "shoes"
    And Click "search" button
    Then Filter "US Shoe Size" by "10"
    And Filter "Color" by "Black"
    And Filter "Occasion" by "Casual"
    And Filter "Upper Material" by "Fabric"
    And Filter "Brand" by "adidas"
    And Filter "Condition" by "New with tags"
    And Filter "Price" by "Under $75.00"
    And Filter "Buying Format" by "Buy It Now"
    And Filter "Delivery Options" by "Free International Shipping"
    And Filter "Show only" by "Free Returns"

  Scenario: Search validation
    Given Navigate to ebay
    And In search bar type "shoes"
    And Click "search" button
    Then All items are "shoes" related

  Scenario Outline: Header navigation check
    Given Navigate to ebay
    And Click "<header link>" link
    Then Make sure we land on "<desired_page>"

  Examples:
    | header link  | desired_page |
    | Daily Deal   | Daily Deal   |
    | Brand Outlet | Brand Outlet |
    | Gift Cards   | Gift Cards   |

  Scenario: Check big text
    Given Navigate to ebay
    And Click "Accessibility" link page
    Then Check text of policy
    """
    eBay Inc. is committed to building a community enabled by people and supported by technology that’s open to the broadest audience possible.
    """

  Scenario: Structured data as a variable
    Given Navigate to ebay
    And In search bar type "shoes"
    And Click "search" button
    Then Checking filters through table data
    | filter_name      | filter_value                |
    | US Shoe Size     | 10                          |
    | Color            | Black                       |
    | Occasion         | Casual                      |
    | Upper Material   | Fabric                      |
    | Brand            | adidas                      |
    | Condition        | New with tags               |
    | Price            | Under $75.00                |
    | Buying Format    | Buy It Now                  |
    | Delivery Options | Free International Shipping |
    | Show only        | Free Returns                |

  Scenario: Validate Search functionality on few pages when landed on the page "5" till page "2"
    Given Navigate to ebay
    And In search bar type "shoes"
    And Click "search" button
    Then Starting with page "5" validate result "shoes" till page "2"