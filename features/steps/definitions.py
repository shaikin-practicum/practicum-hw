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