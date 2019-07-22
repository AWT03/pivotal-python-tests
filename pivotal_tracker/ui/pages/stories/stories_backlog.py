from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.tabs.user_main_tabs import UserMainTabs

add_story_backlog = 'div[id*="panel_backlog"] a[class*="FirstStoryAddButton"]'
story_title = 'textarea[name*="story"]'
save_button = 'button[class*="autosaves button"]'
cancel_button = 'button[class*="autosaves cancel"]'
add_task = 'div[data-aid*="Tasks"] span[class*="AddSubresourceButton__message"]'
task_title = 'textarea[placeholder*="Add a task"]'
add_button = 'button[data-aid*="addTaskButton"]'


class StoriesBacklog(ActionPage, FormPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "story_title": lambda value: self.set_value(story_title, value),
            "task_title": lambda value: self.set_task(value)
        }
        actions = {
            "Save": lambda: self.click(save_button),
            "Cancel": lambda: self.click(cancel_button),
            "Add a Task": lambda: self.click(add_task),
            "Add": lambda: self.click(add_button),
            "Task": lambda: self.is_existing(add_task)
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

    def set_task(self, value):
        self.click(add_task)
        self.set_value(task_title, value)
        self.click(add_button)
