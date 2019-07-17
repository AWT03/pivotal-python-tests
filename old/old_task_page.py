from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage

add_new_task_field = '[data-type="icebox"] [class="tasks full"] textarea[placeholder="Add a task"]'
add_new_task_button = '[data-type="icebox"] [class="tasks full"] button[data-aid="addTaskButton"]'
task_description_field = '[data-type="icebox"] [class="tasks full"] div[data-aid="Tasks"] ' \
                         'div[data-aid="TaskShow"] span:nth-child(1) p'
task_count = '[data-aid="Tasks"] [data-aid="taskCounts"] h4'
delete_task_button = '[data-type="icebox"] [class="tasks full"] div[data-aid="Tasks"] ' \
                     'div[data-aid="TaskShow"] button[data-aid="delete"]'
edit_task_field = '[data-type="icebox"] [class="tasks full"] textarea[data-aid="editor"]'
save_task_updated_button = '[data-type="icebox"] [class="tasks full"] div[data-aid="Tasks"] ' \
                           'button[data-aid="saveTaskButton"]'


class TaskPage(FormPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "description": lambda type_action, value: self.set_name_task(type_action, value)
        }
        actions = {
            "Add": lambda: self.add_task(),
            "Delete": lambda: self.delete_task(),
            "Save": lambda: self.save_task_updated(),
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

    def set_name_task(self, type_action, value):
        if type_action != 'update':
            self.set_value(add_new_task_field, value)
        else:
            self.set_value(edit_task_field, value)

    def add_task(self):
        self.click(add_new_task_button)
        return TaskPage(self.get_driver())

    def verify_description(self):
        return self.get_value(task_description_field)

    def get_count_task_value(self):
        return self.get_value(task_count)

    def delete_task(self):
        self.click(delete_task_button)
        return TaskPage(self.get_driver())

    def get_element(self):
        element = None
        try:
            element = self.find_element(task_description_field)
        except:
            pass
        return element

    def save_task_updated(self):
        self.click(save_task_updated_button)
        return TaskPage(self.get_driver())