from behave import given
from os.path import join
from core.features.steps.functions import *
from pivotal_tracker.pivotal_tracker_dir import pivotal_tracker_path


# This way of logging as user is proper of Pivotal Tracker
@given('I log in as user {user_id}')
def step_impl(context, user_id):
    pivotal_config = get_config(join(pivotal_tracker_path, "config.json"))
    context.api.set_config(pivotal_config)
    context.headers = pivotal_config.get("USER").get(str(user_id))
