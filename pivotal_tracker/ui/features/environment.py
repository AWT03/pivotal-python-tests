from pivotal_tracker.api.features.steps.functions import delete_items


def after_all(context):
    delete_items('projects')


def before_all(context):
    delete_items('projects')


def after_scenario(context, scenario):
    # driver is being closed here because we login in each scenario
    # when only we login only once it should be closed in after all hook method
    close_driver(context)
    if scenario.tags:
        clean_response_value(context, scenario)
        clean_projects(scenario)


def clean_response_value(context, scenario):
    if "clean_response" in scenario.tags:
        context.save_response = None
        context.data_verify = None


def clean_projects(scenario):
    if "clean_projects" in scenario.tags:
        delete_items('projects')


def close_driver(context):
    if context.page is not None:
        context.page.get_driver().quit()
