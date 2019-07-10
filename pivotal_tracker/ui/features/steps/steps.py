from behave import given, when, then, step
from json import loads
from os.path import join
from time import sleep
from pivotal_tracker.ui.util.format_string import format_string
from core.ui.utils.set_up_driver import set_up_driver
from pivotal_tracker.ui.pivotal_tracker_dir import pivotal_tracker_path
from pivotal_tracker.ui.pages.login_page import LoginPage

CONFIG = loads(open(join(pivotal_tracker_path, 'config.json')).read())


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


@step('I exist')
def step_impl(context):
    sleep(3)
    assert True is not False
