from behave import given, step
from json import loads
from os.path import join
from core.ui.utils.set_up_driver import set_up_driver
from pivotal_tracker.ui.pivotal_tracker_dir import pivotal_tracker_ui_path
from pivotal_tracker.ui.pages.login_page import LoginPage


CONFIG = loads(open(join(pivotal_tracker_ui_path, 'config.json')).read())


@given('I login the app as {username}')
def step_impl(context, username):
    context.page = LoginPage(set_up_driver(CONFIG))
    context.page.set_form(sign_in_as=CONFIG.get("USERS").get(username).get("username"),
                          password=CONFIG.get("USERS").get(username).get("password"))
    context.page = context.page.do_action("Sign In")
