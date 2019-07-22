from core.ui.pages.action_page import ActionPage

story_title = 'textarea[name*="story"]'
save_button = 'button[class*="autosaves button"]'
cancel_button = 'button[class*="autosaves cancel"]'
add_task = 'div[data-aid*="Tasks"] span[class*="AddSubresourceButton__message"]'
task_title = 'textarea[placeholder*="Add a task"]'
add_button = 'button[data-aid*="addTaskButton"]'


class ProjectStories(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_form(self, values):
        pass
