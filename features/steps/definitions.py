from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By


@step('Navigate to ebay')
def test(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("https://www.ebay.com")


@step('In search bar type "shoes"')
def search_items(context):
    search = context.browser.find_element(By.XPATH, "//input[@placeholder = 'Search for anything']")
    search.send_keys("shoes")


@step('Click "search" button')
def click_search(context):
    press_search = context.browser.find_element(By.XPATH, "//input[@type = 'submit']")
    press_search.click()


@step('All displayed items are relevant to keyword "shoes"')
def verify_results_shoes_items(context):
    results = context.browser.find_element(By.XPATH, "//span[contains(text(), 'Shoes')]")


@step('Click "Daily Deal" link')
def click_daily_deal_link(context):
    click_daily_deal = context.browser.find_element(By.XPATH, "//a[@class = 'gh-p' and text() = ' Daily Deals']")
    click_daily_deal.click()


@step('All displayed items are relevant to "Daily Deals"')
def verify_results_daily_deals_items(context):
    daily_deals_items = context.browser.find_element(By.XPATH, "//span[contains(text(), ' off')]")


@step('Click "Brand Outlet" link')
def click_brand_outlet_link(context):
    click_brand_outlet = context.browser.find_element(By.XPATH, "//a[text() = ' Brand Outlet']")
    click_brand_outlet.click()


@step('All displayed items are relevant to "Brand Outlet"')
def verification_brand_outlet(context):
    verify_results_brand_outlet_items = context.browser.find_element(By.XPATH, "//div[contains(text(), 'brand')]")
