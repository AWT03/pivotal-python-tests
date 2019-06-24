# After each scenario we will be deleting all data that was created
def after_scenario(context, scenario):
    if scenario:
        context.execute_steps('''
        Then delete urls marked to delete
        ''')
