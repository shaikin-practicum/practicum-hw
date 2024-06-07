from behave import step
from selenium.webdriver import ActionChains
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


@step('Carousel: slides are switching')
def carousel_slides_default(context):
    carousel_slides = WebDriverWait(context.browser, 10).until(EC.presence_of_all_elements_located(
        (By.XPATH, f"//div[contains(@class, 'tracking')]")))
    print(f'There are {len(carousel_slides)} slides in the carousel')
    wait = WebDriverWait(context.browser, 4 * len(carousel_slides))
    for slide in carousel_slides:
        # visible
        wait.until(EC.visibility_of(slide), message=f'Slide {carousel_slides.index(slide)} wasn\'t visible')
        # invisible
        wait.until(EC.invisibility_of_element(slide), message=f'Slide {carousel_slides.index(slide)} remained visible')
        print(f'Slide {carousel_slides.index(slide)} is fine')


@step('Navigate to {direction} slide')
def navigation(context, direction):
    initial_slide = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tracking')]")))
    initial_slide_text = initial_slide.text
    button = WebDriverWait(context.browser, 1).until(EC.presence_of_element_located(
        (By.XPATH, f"//button[@aria-label = 'Go to {direction} banner']")))
    button.click()
    sleep(1)
    final_slide = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tracking')]")))
    final_slide_text = final_slide.text
    if initial_slide_text != final_slide_text:
        print(f'Button {direction} is working')
    else:
        raise Exception(f'Button {direction} is not working')


@step('Carousel: "{btn}" button')
def carousel_controls(context, btn):
    action_button = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, f"//button[@aria-label = '{btn} Banner Carousel']")))
    action_button.click()
    ActionChains(context.browser).move_by_offset(10, 10).perform()


@step('Carousel: slides are paused')
def carousel_slides_paused(context):
    initial_slide = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tracking')]")))
    initial_slide_text = initial_slide.text
    sleep(5)
    final_slide = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tracking')]")))
    final_slide_text = final_slide.text
    if initial_slide_text == final_slide_text:
        print('Slides in carousel are not moving')
    else:
        raise Exception("Slides in carousel are still moving")


@step('Check filters and validate that all items related those filters')
def test_filter(context):
    for row in context.table:
        filter_name = row['filter_name']
        filter_value = row['filter_value']
        filter_checkbox = context.browser.find_element(By.XPATH, f"//li[@class = 'x-refine__main__list ']"
                                                                 f"[.//div[text() = '{filter_name}']]"
                                                                 f"//input[@* = '{filter_value}']")
        filter_checkbox.click()
    all_items = context.browser.find_elements(By.XPATH, f"//li[contains(@id, 'item')]")
    main_window = context.browser.current_window_handle
    wait = WebDriverWait(context.browser, 10)
    issues = []
    for item in all_items:
        item_title = item.find_element(By.XPATH, ".//span[@role = 'heading']").text
        item_url = item.find_element(By.XPATH, ".//a[@class = 's-item__link']").get_attribute('href')
        context.browser.execute_script(f"window.open('{item_url}')")
        context.browser.switch_to.window(context.browser.window_handles[-1])
        all_labels = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//dt[@class = 'ux-labels-values__labels']")))
        all_values = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//dd[@class = 'ux-labels-values__values']")))

        all_labels_text = []
        for label in all_labels:
            all_labels_text.append(label.text)

        all_values_text = []
        for value in all_values:
            all_values_text.append(value.text)

        item_specs = dict(zip(all_labels_text, all_values_text))

        for row in context.table:
            filter_name = row['filter_name']
            filter_value = row['filter_value']

            if filter_name not in item_specs.keys():
                issues.append(f'{item_title} does not have anything related to {filter_name}')
            elif item_specs[filter_name] != filter_value:
                issues.append(f'{item_title} is not related to {filter_value} by {filter_name}')

        context.browser.close()

        context.browser.switch_to.window(main_window)

    if issues:
        raise Exception(f'Following issues discovered: \n{issues}')
