from behave import *
from selenium import webdriver
from selenium.webdriver.common import keys

use_step_matcher("re")


@given("I am on google search page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("serach page")

    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.co.uk")
     



@when("I type in text to search")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("serach page")

    context.driver.find_element_by_tag_name('input[name=q]').send_keys('hi how are you')

    # driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_tag_name('input[name=q]').send_keys(u'\ue007')


@step("I hit search button")
def step_impl(context):
    """
    :type context: behave.runner.Context  result-stats
    """
    print("serach page")


@then("I should be on the search result page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    rest = context.driver.find_element_by_id('result-stats').text
    print(rest)

