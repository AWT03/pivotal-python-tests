from pivotal_tracker.features.steps import functions as func


# After each scenario we will be deleting all data that was created
def after_scenario(context, scenario):
    if scenario:
        context.execute_steps('''
        Then delete urls marked to delete
        ''')
    func.delete_items('projects')

def after_all(context):
    func.delete_items('projects')


# This will be executed at the beginning of the all scenarios only once
def before_all(context):
    func.delete_items('projects')
