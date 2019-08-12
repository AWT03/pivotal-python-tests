from behave import given, step
from json import loads
from os.path import join
from core.ui.utils.set_up_driver import set_up_driver
from pivotal_tracker.ui.pivotal_tracker_dir import pivotal_tracker_ui_path
from pivotal_tracker.ui.pages.login_page import LoginPage
from pivotal_tracker.ui.util.format_string import format_string
import pivotal_tracker.api.features.steps.custom_steps
import core.api.features.steps.steps
from pivotal_tracker.ui.features.steps.functions import *
from pivotal_tracker.ui.pages.dashboard.dashboard_page import DashboardPage


CONFIG = loads(open(join(pivotal_tracker_ui_path, 'config.json')).read())


def get_last_set_values(context):
    context.last_set_values = {}
    for row in context.table.rows:
        context.last_set_values[row[0]] = format_string(row[1]) if isinstance(row[1], str) else row[1]


@step("I save {feature}")
def step_impl(context, feature):
    api_response = loads(context.api.get_full_response())
    context.save_names[feature] = api_response['name']


@step('I click on {feature} created by API')
def step_impl(context, feature):
    context.page.do_action(feature, context.save_names)


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
    if "projects_dashboard" not in context.page.get_search_keys():
        context.page.get_tab()
    context.page.do_action("Create Project")
    get_last_set_values(context)
    context.page.go_to("ProjectCreation")
    context.page.get_tab().set_form(**context.last_set_values)
    context.page.do_action("Create")


@step('I create a project on project list with')
def step_impl(context):
    assert context.table is not None
    context.page.get_tab().do_action("Create Project")
    get_last_set_values(context)
    context.page.go_to("ProjectCreation")
    context.page.get_tab().set_form(**context.last_set_values)
    context.page.do_action("Create")


@step('I create a project on main header with')
def step_impl(context):
    assert context.table is not None
    context.page.context.get_tab().do_action("Create Project")
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


@step('I do click on {button} button')
def step_impl(context, button):
    context.page.get_tab().get_tab().do_action(button)
    context.page.set_tab(DashboardPage(context.page.get_driver()))


@step('I verify {word} is displayed on {key}')
def step_impl(context, word, key):
    if key not in context.page.get_search_keys():
        tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    else:
        tab = context.page
    if word in context.last_set_values:
        exists = tab.is_displayed_as(key, context.last_set_values[word])
    else:
        exists = tab.is_displayed_as(key, word)
    assert exists is True


@step('Check {task} box as completed')
def step_impl(context, task):
    if 'complete_task' not in context.page.get_search_keys():
        tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    else:
        tab = context.page
    exists = tab.is_displayed_as('complete_task', context.last_set_values[task])
    assert exists is True


@step('I open the {name} project')
def step_impl(context, name ):
    if "access_project" not in context.page.get_search_keys():
        tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    else:
        tab = context.page
    tab.is_displayed_as("access_project", context.save_names["project_name"])


@step('I expand the {name} story')
def step_impl(context, name):
    if "expand_story" not in context.page.get_search_keys():
        tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    else:
        tab = context.page
    if name == "story_name":
        tab.is_displayed_as("expand_story", context.save_names["story_name"])
    else:
        tab.is_displayed_as("expand_story", context.last_set_values["story_title"])


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
    if "last_set_values" in context:
        context.page.do_action(button, context.last_set_values[key])
        context.tab_level = context.page.get_tab_level()
    else:
        key_split = key.split('_')
        context.last_set_values = loads(context.api.get_full_response())
        context.page.do_action(button, context.last_set_values[key_split[1]])
        context.tab_level = context.page.get_tab_level()


@step('I do click over {button} of the {key}')
def step_impl(context, button, key):
    if "last_set_values" in context:
        context.page.do_action(button, context.last_set_values[key])
        context.tab_level = context.page.get_tab_level()
    else:
        key_split = key.split('_')
        context.last_set_values = loads(context.api.get_full_response())
        context.page.get_tab().do_action(button, context.last_set_values[key_split[1]])
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
    context.page.go_to("WorkspaceMain");
    context.page.get_tab().do_action("Open Workspace Settings")


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


@step('I update a workspace with2')
def step_impl(context):
    assert context.table is not None
    get_last_set_values(context)
    eval('context.page' + ''.join((context.page.get_tab_level() + 1) *
                                  ['.get_tab()']) + '.set_form(**context.last_set_values)')
    context.page.do_action("Save")


@step('I open the Workspace Name')
def step_impl(context):
    last_name_workspace = loads(context.api.get_full_response())["name"]
    context.last_set_values = context.api.get_full_response()
    context.page.get_tab().get_tab().do_action('Workspace name', last_name_workspace)
    context.tab_level = context.page.get_tab_level()


def get_object_attribute_value(context, type_attribute, type_object):
    response = context.save_response
    object_attribute_value = ''
    for res in response:
        if res['kind'] == type_object.lower():
            object_attribute_value = res[type_attribute.lower()]
            break
    return object_attribute_value


@step('I verify that "{message}" message is displayed for "{object_attribute}"')
def step_impl(context, message, object_attribute):
    tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    object_attribute_split = object_attribute.split('_')
    if not isinstance(context.last_set_values, dict):
        response = tab.is_displayed_as(message, loads(context.last_set_values)[object_attribute_split[1]])
    else:
        response = tab.is_displayed_as(message, context.last_set_values[object_attribute_split[1]])
    assert response == 1


@step("I verify {key} is not displayed on {selector}")
def step_impl(context, key, selector):
    key_split = key.split('_')
    if selector not in context.page.get_search_keys():
        tab = eval('context.page' + ''.join((context.tab_level+1) * ['.get_tab()']))
    else:
        tab = context.page
    if not isinstance(context.last_set_values, dict):
        exists = tab.is_displayed_as(selector, loads(context.last_set_values)[key_split[1]])
    else:
        exists = tab.is_displayed_as(selector, context.last_set_values[key_split[1]])
    assert exists is False
