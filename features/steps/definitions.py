from behave import step
from selenium import webdriver


@step('Navigate to Google')
def test(context):
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
