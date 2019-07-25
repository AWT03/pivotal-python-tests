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


@step('I create an account with name {account_name}')
def step_impl(context, account_name):
    new_account_name = format_string(account_name)
    context.page.do_action("Create Account", new_account_name)
    context.last_set_values = {"account_name": new_account_name}


@step('I modify project settings with')
def step_impl(context):
    assert context.table is not None
    context.last_set_values = {}
    for row in context.table.rows:
        context.last_set_values[row[0]] = format_string(row[1]) if isinstance(row[1], str) else row[1]
    context.page.get_tab().get_tab().set_form(**context.last_set_values)
    context.page.do_action("Save")


@step('I go to {navigation}')
def step_impl(context, navigation):
    if navigation.split('->')[0]:
        for index, tab in enumerate(navigation.split('->')):
            eval("context.page" + ''.join(index*['.get_tab()']) + ".go_to(tab)")
    else:
        tabs = len(navigation.split('->'))-1
        tab_levels = context.page.get_tab_level()
        current = eval("context.page" + ''.join((tab_levels - tabs) * ['.get_tab()']))
        for index, tab in enumerate(navigation.split('->')[1:]):
            current = eval("current" + ''.join((index+1)*['.get_tab()']))
            current.go_to(tab)
    context.tab_level = context.page.get_tab_level()


@step('I create a story with')
def step_impl(context):
    assert context.table is not None
    context.page.do_action("Add Story")
    context.last_set_values = {}
    for row in context.table.rows:
        context.last_set_values[row[0]] = format_string(row[1]) if isinstance(row[1], str) else row[1]
    context.page.get_tab().get_tab().set_form(**context.last_set_values)
    context.page.do_action("Save")


@step('I click on {button}')
def step_impl(context, button):
    context.page.do_action(button)


@step('I verify project name is displayed on header')
def step_impl(context):
    assert context.page.validate_name(context.last_set_values["project_name"]) is True


@step('I verify {word} is displayed on {key}')
def step_impl(context, word, key):
    tab = eval('context.page' + ''.join(context.tab_level * ['.get_tab()']))
    exists = tab.is_displayed_as(key, context.last_set_values[word])
    assert exists is True


@step('I verify {key} element {assertion} displayed')
def step_impl(context, key, assertion):
    exist = context.page.is_existing(key)
    if assertion == "is not":
        assert exist is False
    else:
        assert exist is True


@step('I verify my projects counter is counting all projects')
def step_impl(context):
    tab = eval('context.page' + ''.join(context.tab_level * ['.get_tab()']))
    projects = tab.number_projects()
    exists = tab.project_counter(str(projects))
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


@step('I select Manage Account for recently created')
def step_impl(context):
    context.page.do_action("Manage Account", context.last_set_values["account_name"])


@step('I exist {seconds}')
def step_impl(context, seconds):
    from time import sleep
    sleep(int(seconds))
