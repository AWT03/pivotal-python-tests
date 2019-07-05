from behave import given, then, when
from pivotal_tracker.features.steps.functions import *
from pivotal_tracker.pivotal_tracker_dir import pivotal_tracker_path
from pivotal_tracker.pivotal_tracker_api import PivotalTrackerApi

path_data_files = get_config(join(pivotal_tracker_path, 'config.json'))['PATH_DATA_FILES']


# This way of logging as user is proper of Pivotal Tracker
@given('I log in as user {user_name}')
def step_impl(context, user_name):
    pivotal_config = get_config(join(pivotal_tracker_path, "config.json"))
    pivotal_message = get_config(join(pivotal_tracker_path, "message.json"))
    context.api.set_config(pivotal_config)
    context.api.set_message(pivotal_message)
    if not context.headers:
        context.headers = {}
    user_config = pivotal_config.get("USER").get(user_name)
    context.headers[pivotal_config.get("TOKEN_HEADER")] = user_config.get("TOKEN")
    context.user_id = user_config.get("ID")
    context.path_data_files = join(pivotal_tracker_path, pivotal_config.get("PATH_DATA_FILES"))

# This way of logging as user is proper of Pivotal Tracker
@when('I log in as user {user_name}')
def step_impl(context, user_name):
    pivotal_config = get_config(join(pivotal_tracker_path, "config.json"))
    pivotal_message = get_config(join(pivotal_tracker_path, "message.json"))
    context.api.set_config(pivotal_config)
    context.api.set_message(pivotal_message)
    if not context.headers:
        context.headers = {}
    user_config = pivotal_config.get("USER").get(user_name)
    context.headers[pivotal_config.get("TOKEN_HEADER")] = user_config.get("TOKEN")
    context.user_id = user_config.get("ID")
    context.path_data_files = join(pivotal_tracker_path, pivotal_config.get("PATH_DATA_FILES"))


@given('I start a connection with the Pivotal Tracker API')
def step_impl(context):
    api = PivotalTrackerApi()
    context.api = api
    context.to_delete = []
    context.saved_ids = ['']
    context.path_data_files = path_data_files
    context.headers = None
    context.ids_list = []
    context.save_response = []
# <<<<<<< HEAD


@then('I expect the {kind} message {message_tag}')
def step_imp(context, kind, message_tag):
    assert context.text is None
    api_response = loads(context.api.get_full_response())
    assert api_response is not None
    message = get_message(message_tag)
    assert message is not None
    for tag in message:
        assert tag in api_response
        assert api_response[tag] == message[tag]
# =======
#     context.ids_list = []
#     context.save_response = []
#     context.data = None
# >>>>>>> 53401559b449d8342a8e241fb26444de88cc47e6
