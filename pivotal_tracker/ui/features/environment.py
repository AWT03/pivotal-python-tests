from pivotal_tracker.api.features.steps.functions import delete_items
import logging


def after_all(context):
    delete_items('projects')
    delete_items('my/workspaces')


def before_all(context):
    # context.config.setup_logging()
    # -- SAME-AS:
    # import logging
    # logging.basicConfig(level=context.config.logging_level)
    context.config.setup_logging(filename="debug.log", level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    delete_items('projects')
    delete_items('my/workspaces')


def after_scenario(context, scenario):
    # driver is being closed here because we login in each scenario
    # when only we login only once it should be closed in after all hook method
    close_driver(context)
    if scenario.tags:
        clean_projects(scenario)
        clean_workspaces(scenario)


def clean_projects(scenario):
    if "clean_projects" in scenario.tags:
        delete_items('projects')


def clean_workspaces(scenario):
    if "clean_workspaces" in scenario.tags:
        delete_items('my/workspaces')


def close_driver(context):
    if context.page is not None:
        context.page.get_driver().quit()
