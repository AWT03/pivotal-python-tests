from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.pages.element_search import Element
from core.ui.pages.element_search import ElementSearch

add_story_backlog = 'div[id*="panel_backlog"] a[class*="FirstStoryAddButton"]'
story_title = 'textarea[name*="story"]'
save_button = 'button[class*="autosaves button"]'
cancel_button = 'button[class*="autosaves cancel"]'
add_task = 'div[data-aid*="Tasks"] span[class*="AddSubresourceButton__message"]'
task_title = 'textarea[placeholder*="Add a task"]'
add_button = 'button[data-aid*="addTaskButton"]'
expand_story = 'div[aria-label="$(story_name)"] button'
label = 'input[placeholder*="Add a label"]'
description = 'textarea[data-focus-id*="DescriptionEdit"]'
comment = 'textarea[data-aid*="Comment__textarea"]'


class StoriesBacklog(ActionPage, FormPage,ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        search_elements = {
            "access_story": lambda value: self.open_story(value),
        }
        fields = {
            "story_title": lambda value: self.set_value(story_title, value),
            "task_title": lambda value: self.set_task(value),
            "label": lambda value: self.set_value(label, value),
            "description": lambda value: self.set_value(description, value),
            "comment": lambda value: self.set_value(comment, value)
        }
        actions = {
            "Add Story": lambda: self.click(add_story_backlog),
            "Save": lambda: self.click(save_button),
            "Cancel": lambda: self.click(cancel_button),
            "Add a Task": lambda: self.click(add_task),
            "Add": lambda: self.click(add_button),
            "Task": lambda: self.is_existing(add_task)
        }
        self.update_search_fields(**search_elements)
        self.update_actions(**actions)
        self.update_form_fields(**fields)

    def set_task(self, value):
        self.click(add_task)
        self.set_value(task_title, value)
        self.click(add_button)

    def open_story(self, name):
        self.click(expand_story.replace('$(story_name)', name))


