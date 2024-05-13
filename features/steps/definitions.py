from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


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


@step('All displayed items are relevant to {tag} and {class_one} and {v_one} and {class_two} and {v_two}')
def verify_items(context, tag, class_one, v_one, class_two, v_two):
    item = context.browser.find_element(By.XPATH, f"//{tag}[@{class_one} = {v_one} and contains({class_two}, {v_two})]")
    item.click()
    sleep(5)


@step('Click {box} link')
def click_link(context, box):
    link = context.browser.find_element(By.XPATH, f"//*[contains(@class, 'gh-') and contains(text(), {box})]")
    link.click()
