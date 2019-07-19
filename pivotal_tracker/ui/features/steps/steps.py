from behave import given, step
from json import loads
from os.path import join
from core.ui.utils.set_up_driver import set_up_driver
from pivotal_tracker.ui.pivotal_tracker_dir import pivotal_tracker_ui_path
from pivotal_tracker.ui.pages.login_page import LoginPage
from pivotal_tracker.ui.util.format_string import format_string


CONFIG = loads(open(join(pivotal_tracker_ui_path, 'config.json')).read())


@given('I login the app as {username}')
def step_impl(context, username):
    context.tab_level = 0
    context.page = LoginPage(set_up_driver(CONFIG))
    context.page.set_form(sign_in_as=CONFIG.get("USERS").get(username).get("username"),
                          password=CONFIG.get("USERS").get(username).get("password"))
    context.page = context.page.do_action("Sign In")


@step('I create a project with')
def step_impl(context):
    assert context.table is not None
    context.page.do_action("Create Project")
    context.last_set_values = {}
    for row in context.table.rows:
        context.last_set_values[row[0]] = format_string(row[1]) if isinstance(row[1], str) else row[1]
    context.page.go_to("ProjectCreation")
    context.page.get_tab().set_form(**context.last_set_values)
    context.page.do_action("Create")


@step('I go to {navigation}')
def step_impl(context, navigation):
    context.tab_level = len(navigation.split('->'))
    for index, tab in enumerate(navigation.split('->')):
        eval("context.page" + ''.join(index*['.get_tab()']) + ".go_to(tab)")


@step('I verify project name is displayed on header')
def step_impl(context):
    assert context.page.validate_name(context.last_set_values["project_name"]) is True


@step('I verify {word} is displayed on {key}')
def step_impl(context, word, key):
    tab = eval('context.page' + ''.join(context.tab_level * ['.get_tab()']))
    exists = tab.is_displayed_as(key, context.last_set_values[word])
    assert exists is True


@step('I verify project name is displayed')
def step_impl(context):
    tab = eval('context.page' + ''.join(context.tab_level * ['.get_tab()']))
    exists = tab.project_exists(context.last_set_values["project_name"])
    assert exists is True


@step('I verify project settings were created according to characteristics')
def step_impl(context):
    assert context.page.get_tab().get_tab().\
        match_fields(**context.last_set_values) is True
