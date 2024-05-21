from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@step('Navigate to ebay')
def test(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("https://www.ebay.com")


@step('In search bar type "{item}"')
def search_items(context, item):
    search = context.browser.find_element(By.XPATH, "//input[@placeholder = 'Search for anything']")
    search.send_keys(f"{item}")


@step('Click "search" button')
def click_search(context):
    press_search = context.browser.find_element(By.XPATH, "//input[@type = 'submit']")
    press_search.click()


@step('Click {box} link')
def click_link(context, box):
    link = context.browser.find_element(By.XPATH, f"//*[contains(@class, 'gh-') and contains(text(), {box})]")
    link.click()


@step('All displayed items are relevant to {v_one} and {v_two}')
def verify_items(context, v_one, v_two):
    item = context.browser.find_element(By.XPATH, f"//*[@* = {v_one} and contains(., {v_two})]")


@step('Filter "{filter_name}" by "{value}"')
def filter_items(context, filter_name, value):
    filter_option = context.browser.find_element(By.XPATH, f"//li[@class = 'x-refine__main__list ']"
                                                           f"[.//div[text() = '{filter_name}']]//input[@* = '{value}']")
    filter_option.click()
    sleep(3)


@step('All items are "{desired_title}" related')
def check_all_item_title(context, desired_title):
    issues = []
    for page in range(2):
        all_items = context.browser.find_elements(By.XPATH, "//li[contains(@id, 'item')]//span[@role = 'heading']")
        for item in all_items:
            title = item.text
            if desired_title.lower() not in title.lower():
                issues.append(f'{title} is not {desired_title} related')
        next_page = context.browser.find_element(By.XPATH, "//a[@type = 'next']")
        next_page.click()

    if issues:
        raise Exception(f'Following issues discovered: \n{issues}')


@step('Make sure we land on "{desired_page}"')
def make_sure_page(context, desired_page):
    current_page = context.browser.title
    if desired_page.lower() not in current_page.lower():
        raise Exception(f'Page {desired_page} not found on {current_page}')

