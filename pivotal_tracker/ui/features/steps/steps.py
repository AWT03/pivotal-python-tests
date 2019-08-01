from behave import given, step
from json import loads
from os.path import join
from core.ui.utils.set_up_driver import set_up_driver
from pivotal_tracker.ui.pivotal_tracker_dir import pivotal_tracker_ui_path
from pivotal_tracker.ui.pages.login_page import LoginPage
from pivotal_tracker.ui.util.format_string import format_string

CONFIG = loads(open(join(pivotal_tracker_ui_path, 'config.json')).read())


def get_last_set_values(context):
    context.last_set_values = {}
    for row in context.table.rows:
        context.last_set_values[row[0]] = format_string(row[1]) if isinstance(row[1], str) else row[1]


@step('I login the app as {username}')
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
    get_last_set_values(context)
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
    get_last_set_values(context)
    context.page.get_tab().get_tab().set_form(**context.last_set_values)
    context.page.do_action("Save")


@step('I click on {button}')
def step_impl(context, button):
    context.page.do_action(button)


@step('I verify {word} is displayed on {key}')
def step_impl(context, word, key):
    if key not in context.page.get_search_keys():
        tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    else:
        tab = context.page
    exists = tab.is_displayed_as(key, context.last_set_values[word])
    assert exists is True


@step('I verify that {key} is displayed as {value}')
def step_impl(context, key, value):
    print(context.tab_level)
    tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    exists = tab.is_displayed_as(key, value)
    assert exists is True


@step('I verify {key} element {assertion} displayed')
def step_impl(context, key, assertion):
    exist = context.page.is_existing(key)
    if assertion == "is not":
        assert exist is False
    else:
        assert exist is True


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


@step('I create a workspace with')
def step_impl(context):
    assert context.table is not None
    context.page.do_action("Create workspace")
    get_last_set_values(context)
    context.page.get_tab().set_form(**context.last_set_values)
    context.page.do_action("Create")


@step('I verify that workspace settings were created according to characteristics')
def step_impl(context):
    assert eval('context.page' + ''.join((context.page.get_tab_level()+1) * ['.get_tab()'])+
                '.match_fields(**context.last_set_values)') is True


@step('I verify that project counter is equal to {counter}')
def step_impl(context, counter):
    tab = eval('context.page' + ''.join(context.tab_level * ['.get_tab()']))
    assert tab.validate_project_counter(counter) is True


@step('I verify this message {message} is displayed for this {tag}')
def step_impl(context, message, tag):
    tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    assert tab.validate_sms_in_workspace(message, context.last_set_values[tag]) is True


@step('I verify that {option} option is visible')
def step_impl(context, option):
    tab = eval('context.page' + ''.join(context.tab_level * ['.get_tab()']))
    assert tab.validate_option_displayed(option) is True


@step('I do click on {button} of the {key}')
def step_impl(context, button, key):
    context.page.do_action(button, context.last_set_values[key])
    context.tab_level = context.page.get_tab_level()


@step('I verify that "{word}" is displayed for {key}')
def step_impl(context, word, key):
    tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    assert tab.is_displayed_as("project_colors", word.replace("\'", ""),
                               context.last_set_values[key]) is True


@step('I verify {counter} projects is displayed for {key}')
def step_impl(context, counter, key):
    tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    value_counter = tab.is_displayed_as("projects_counter", context.last_set_values[key])
    value_counter_splitter = value_counter.split()
    assert value_counter_splitter[0] == counter


@step('I open the workspace settings from stories')
def step_impl(context):
    context.page.do_action("Open Workspace Settings")


@step('I verify that "{message}" message is displayed for "{object_attribute}"')
def step_impl(context, message, object_attribute):
    tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    response = tab.is_displayed_as(message, context.last_set_values[object_attribute])
    assert response == 1


@step("I verify {key} is not displayed on {selector}")
def step_impl(context, key, selector):
    if selector not in context.page.get_search_keys():
        tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    else:
        tab = context.page
    exists = tab.is_displayed_as(selector, context.last_set_values[key])
    assert exists is False


@step('I verify that "{message}" message is displayed')
def step_impl(context, message):
    tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    response = tab.verify_save_message(message)
    assert response == 1


@step('I update a workspace with')
def step_impl(context):
    assert context.table is not None
    get_last_set_values(context)
    eval('context.page' + ''.join((context.page.get_tab_level() + 1) * 
                                  ['.get_tab()']) + '.set_form(**context.last_set_values)')
    context.page.do_action("Save")


@step("I save {feature} name")
def step_impl(context, feature):
    print(context.data.text)
