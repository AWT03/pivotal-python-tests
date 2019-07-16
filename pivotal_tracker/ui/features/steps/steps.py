from behave import given, when, then, step
from json import loads
from os.path import join
from time import sleep
from pivotal_tracker.ui.util.format_string import format_string
from core.ui.utils.set_up_driver import set_up_driver
from pivotal_tracker.ui.pivotal_tracker_dir import pivotal_tracker_ui_path
from pivotal_tracker.ui.pages.login_page import LoginPage
import pivotal_tracker.api.features.steps.custom_steps
import core.api.features.steps.steps
from pivotal_tracker.ui.features.steps.functions import *

CONFIG = loads(open(join(pivotal_tracker_ui_path, 'config.json')).read())


@given('I login the app as {username}')
def step_impl(context, username):
    context.page = LoginPage(set_up_driver(CONFIG))
    context.page.set_form(sign_in_as=CONFIG.get("USERS").get("owner").get("username"),
                          password=CONFIG.get("USERS").get("owner").get("password"))
    context.page = context.page.do_action("Sign In")


@step('I click on {action_id} button')
def step_impl(context, action_id):
    context.page = context.page.do_action(action_id)


@when('I fill the form with data')
def step_impl(context):
    assert context.table is not None
    set_values = {}
    for row in context.table.rows:
        set_values[row[0]] = format_string(row[1]) if isinstance(row[1], str) else row[1]
    context.page.set_form(**set_values)
    context.data_verify = set_values


@step('I exist')
def step_impl(context):
    sleep(3)
    assert True is not False


@step('I go to the {object_find} created before through url {url_page}')
def step_impl(context, object_find, url_page):
    response = context.save_response
    object_id_prepared = object_find + '_id'
    object_id = 0
    for res in response:
        if object_id_prepared in res:
            object_id = res[object_id_prepared]
    if object_id != 0:
        current_handler = context.page.get_driver()
        main_page = CONFIG.get("MAIN_PAGE")
        object_url = main_page + url_page + str(object_id)
        object_page = FactoryPage.create_page(object_find, current_handler)
        context.page = object_page
        object_page.go_to_url(object_url)


@step('I click on {type_element} element of the {type_object} {type_attribute} on {type_panel} panel')
def step_impl(context, type_element, type_attribute, type_object, type_panel):
    value_attribute = get_object_attribute_value(context, type_attribute, type_object)
    action_id = '{0} {1} {2} {3}'.format(type_element, type_object, type_attribute, type_panel)
    context.page = context.page.do_action_with_value(action_id, value_attribute)


@step('I verify that field {object_attribute} is displayed in the panel')
def step_impl(context, object_attribute):
    object_field_dict = context.data_verify
    object_field = None
    for data in object_field_dict:
        if object_attribute in data:
            object_field = object_field_dict[object_attribute]
    assert object_field is not None
    value_form_story = context.page.verify_description()
    assert object_field == value_form_story


@step('I verify that {count_value} is added to the task counter')
def step_impl(context, count_value):
    value_count_task_all = context.page.get_count_task_value()
    value_count_task_all = value_count_task_all.split('/')
    value_count_task = value_count_task_all[1]
    value_count_task_prepared = value_count_task[-2]
    assert value_count_task_prepared == count_value
