from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage

add_new_task_field = '[data-type="icebox"] [class="tasks full"] textarea[placeholder="Add a task"]'
add_new_task_button = '[data-type="icebox"] [class="tasks full"] button[data-aid="addTaskButton"]'
task_description_field = '[data-type="icebox"] [class="tasks full"] div[data-aid="Tasks"] div[data-aid="TaskShow"] span:nth-child(1) p'
task_count = '[data-aid="Tasks"] [data-aid="taskCounts"] h4'


class TaskPage(FormPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "description": lambda value: self.set_name_task(value)
        }
        actions = {
            "Add": lambda: self.add_task()
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

    def set_name_task(self, value):
        self.set_value(add_new_task_field, value)

    def add_task(self):
        self.click(add_new_task_button)
        return TaskPage(self.get_driver())

    def verify_description(self):
        return self.get_value(task_description_field)

    def get_count_task_value(self):
        return self.get_value(task_count)