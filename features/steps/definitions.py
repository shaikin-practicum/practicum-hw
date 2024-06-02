from behave import step
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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


@step('Click "{accessibility}" link page')
def click_link_policy(context, accessibility):
    policy_link = context.browser.find_element(By.XPATH, f"//a[contains(text(), '{accessibility}')]")
    policy_link.click()


@step('Check text of policy')
def check_text(context):
    desired_text = context.text
    presented_text = context.browser.find_element(By.XPATH, f"//p[contains(text(), '{context.text}')]").text
    if desired_text not in presented_text:
        raise Exception(f'Policy {desired_text} not found on {presented_text}')


@step('Checking filters through table data')
def table_data(context):
    for row in context.table:
        filter_name = row['filter_name']
        filter_value = row['filter_value']
        filter_checkbox = context.browser.find_element(By.XPATH, f"//li[@class = 'x-refine__main__list ']"
                                                                 f"[.//div[text() = '{filter_name}']]"
                                                                 f"//input[@* = '{filter_value}']")
        filter_checkbox.click()


@step('Starting with page "{l_page}" validate result "{desired_title}" till page "{n_pages}"')
def check_all_item_title(context, l_page, desired_title, n_pages):
    issues = []
    landing_page = context.browser.find_element(By.XPATH, f"//a[@class = 'pagination__item' and text() = '{l_page}']")
    landing_page.click()
    current_page = context.browser.find_element(By.XPATH, "//a[@class = 'pagination__item' and @aria-current = 'page']")
    while int(current_page.text) > int(n_pages):
        all_items = context.browser.find_elements(By.XPATH, "//li[contains(@id, 'item')]//span[@role = 'heading']")
        for item in all_items:
            title = item.text
            if desired_title.lower() not in title.lower():
                issues.append(f'{title} is not {desired_title} related')
        previous_page = context.browser.find_element(By.XPATH, "//a[@type = 'previous']")
        previous_page.click()

        current_page = context.browser.find_element(By.XPATH, "//a[@class = 'pagination__item' and "
                                                              "@aria-current = 'page']")

    if issues:
        raise Exception(f'Following issues discovered: \n{issues}')


@step('Checking categories through table data')
def check_categories(context):
    for row in context.table:
        category_name = row['category_name']
        category_path = context.browser.find_element(By.XPATH, f"//a[contains(text(), '{category_name}')]")
        if category_name.lower() not in category_path.text.lower():
            raise Exception(f'Category "{category_name}" not found on "flyout menu"')


@step('Automatic movement')
def find_next_carousel_slide(context):
    next_slide = (WebDriverWait(context.browser, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//ul[@id = 's0-1-0-48-1-2-4-17[0[0]]-0[1]-2-@match-media-0-@ebay-carousel-list'"
                   " and contains(@style, 'transform')]")),
        message="Automatic movement is not working"))
    print(f'Automatic movement is working because {next_slide} is found')


@step('Navigate to {number} slide')
def navigation(context, number):
    button = (WebDriverWait(context.browser, 1).until(EC.presence_of_element_located(
        (By.XPATH, f"//button[@aria-label = 'Go to {number} banner']"))))
    button.click()


@step('Slide is {number} for {action} button')
def slide_checking(context, number, action):
    slide = (WebDriverWait(context.browser, 2).until(EC.presence_of_element_located(
        (By.XPATH, f"//*[contains(@id, '[1]') and contains(@style, 'transform')]/li[{number}]"))))
    if slide.is_displayed():
        print(f"{action} button is working")
    else:
        raise Exception(f"{action} button is not working or slide is not moved")


@step('{action} click')
def actions(context, action):
    action_button = (WebDriverWait(context.browser, 1).until(EC.presence_of_element_located(
        (By.XPATH, f"//button[@aria-label = '{action} Banner Carousel']"))))
    action_button.click()


@step('Check no movement and on the on slide {number} for {action}')
def check_actions(context, number, action):
    current_slide = (WebDriverWait(context.browser, 1).until(EC.presence_of_element_located(
        (By.XPATH, f"//*[contains(@id, '[1]')]/li[{number}]"))))
    if current_slide.is_displayed():
        print(f"{action} button is working")
    else:
        raise Exception(f"{action} button is not working or slide is moved")
