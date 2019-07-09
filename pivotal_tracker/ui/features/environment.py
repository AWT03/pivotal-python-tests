from pivotal_tracker.api.features.steps.functions import delete_items


def after_all(context):
    delete_items('projects')


def before_all(context):
    delete_items('projects')
