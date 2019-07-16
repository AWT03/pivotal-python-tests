from pivotal_tracker.api.features.steps.functions import delete_items


def after_all(context):
    delete_items('projects')


def before_all(context):
    delete_items('projects')


def after_scenario(context, scenario):
    if scenario.tags:
        clean_response_value(context, scenario)


def clean_response_value(context, scenario):
    if "clean_response" in scenario.tags:
        context.save_response = None
        context.data_verify = None