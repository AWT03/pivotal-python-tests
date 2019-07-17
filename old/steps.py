from behave import given, when, then, step
from json import loads
from os.path import join
from pivotal_tracker.ui.util.format_string import format_string
from core.ui.utils.set_up_driver import set_up_driver
from pivotal_tracker.ui.pivotal_tracker_dir import pivotal_tracker_ui_path
from pivotal_tracker.ui.pages.login_page import LoginPage
from pivotal_tracker.ui.features.steps.functions import *


CONFIG = loads(open(join(pivotal_tracker_ui_path, 'config.json')).read())


@given('I login the app as {username}')
def step_impl(context, username):
    context.page = LoginPage(set_up_driver(CONFIG))
    context.page.set_form(sign_in_as=CONFIG.get("USERS").get(username).get("username"),
                          password=CONFIG.get("USERS").get(username).get("password"))
    context.page = context.page.do_action("Sign In")


@step('I verify that {element} does not exist')
def step_impl(context, element):
    exist = context.page.do_action(element)
    print(exist)


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


@step('I open the {type_object} {type_attribute} on {type_panel}')
def step_impl(context, type_object, type_attribute, type_panel):
    value_attribute = get_object_attribute_value(context, type_attribute, type_object)
    action_id = '{0} {1} {2}'.format(type_object, type_attribute, type_panel)
    context.page = context.page.do_action_with_value(action_id, value_attribute)


@step('I verify that "{type_object}" "{object_attribute}" is "{displayed}"')
def step_impl(context, type_object, object_attribute, displayed):
    if displayed == 'displayed':
        object_field_dict = context.data_verify
        object_field = None
        for data in object_field_dict:
            if object_attribute in data:
                object_field = object_field_dict[object_attribute]
        assert object_field is not None
        value_form_story = context.page.verify_description()
        assert object_field == value_form_story
    else:
        task_element = context.page.get_element()
        assert task_element is None


@step('I verify that task counter is "{method}" by "{count_value}"')
def step_impl(context, method, count_value):
    value_count_task_all = context.page.get_count_task_value()
    value_count_task_all = value_count_task_all.split('/')
    value_count_task = value_count_task_all[1]
    value_count_task_prepared = value_count_task[-2]
    if method == 'incremented':
        assert value_count_task_prepared == count_value
    elif method == 'decremented':
        task_counter = 1
        task_counter = task_counter - int(count_value)
        assert value_count_task_prepared == str(task_counter)


@step('I {action_method} the {type_object} {object_attribute}')
def step_impl(context, action_method, type_object, object_attribute):
    action_id = 'Mouse Hover {0} {1}'.format(type_object, object_attribute)
    context.page = context.page.do_action(action_id)
    context.page = context.page.do_action(action_method)


@step('I click on {type_object} {type_attribute} element')
def step_impl(context, type_object, type_attribute):
    value_attribute = get_object_attribute_value(context, type_attribute, type_object)
    action_id = '{0} {1}'.format(type_object, type_attribute)
    context.page = context.page.do_action_with_value(action_id, value_attribute)


@when('I fill the form with data to {type_action}')
def step_impl(context, type_action):
    assert context.table is not None
    set_values = {}
    for row in context.table.rows:
        set_values[row[0]] = format_string(row[1]) if isinstance(row[1], str) else row[1]
    context.page.set_form_action(type_action, **set_values)
    context.data_verify = set_values
