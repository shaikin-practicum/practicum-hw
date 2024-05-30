import os
from selenium import webdriver


def before_feature(context, feature):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()


def before_scenario(context, scenario):
    context.browser.get("https://www.ebay.com")


def after_step(context, step):
    if step.status == 'failed':
        current_dir = os.path.dirname(__file__)
        relative_path_to_dest = os.path.abspath(os.path.join(current_dir, 'failed_screenshots'))
        if not os.path.exists(relative_path_to_dest):
            os.mkdir(relative_path_to_dest)
        context.browser.save_screenshot(os.path.join(relative_path_to_dest, f'{step.name}.png'))
