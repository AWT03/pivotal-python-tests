from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from core.ui.pages.element_search import Element
from core.ui.pages.element_search import ElementSearch

from time import sleep
from selenium.webdriver.common.keys import Keys

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
add_description = '//button[text()="Add description"]'
post_comment = '//button[text()="Post comment"]'
show_edit_description = 'div[class*="DescriptionShow"]'
activity_list = '// div[@data-aid="message"]/span/p[text()="$(comment)"]'
task_list = '// div[@data-aid="TaskDescription"]/span//p[text()="$(task)"]'
task_completed = '//h4[text()="$(counter)"]'
checkbox_task_completed = 'input[title*="mark task complete"]'


class StoriesBacklog(ActionPage, FormPage,ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        search_elements = {
            "expand_story": lambda value: self.open_story(value),
            "title_box": lambda value: self.verify_title_box(value),
            "description_box": lambda value: self.verify_description_box(value),
            "activity_list": lambda value: self.verify_activity_list(value),
            "task_list": lambda value: self.verify_task_list(value),
            "task_counter": lambda value: self.verify_task_counter(value),
            "complete_task": lambda value: self.check_task_complete(value),
        }
        fields = {
            "story_title": lambda value: self.set_value(story_title, value),
            "task_title": lambda value: self.set_task(value),
            "label": lambda value: self.set_value(label, value),
            "description": lambda value: self.add_description(value),
            "comment": lambda value: self.post_comment(value)
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

    def add_description(self, value):
        self.click(show_edit_description)
        self.set_value(description, value)
        #self.click(add_description)

    def post_comment(self, value):
        self.set_value(comment, value)
        self.click(post_comment)

    def add_label(self, value):
        self.set_value(label, value)

    def verify_title_box(self, value):
        if value == self.get_value(story_title):
            return True
        return False

    def verify_description_box(self, value):
        self.click(show_edit_description)
        if value == self.get_value(description):
            return True
        return False

    def verify_activity_list(self, value):
        return self.is_existing(activity_list.replace('$(comment)', value))

    def verify_task_list(self, value):
        return self.is_existing(task_list.replace('$(task)', value))

    def verify_task_counter(self, value):
        value = value.split("/")
        if self.is_existing(task_completed.replace('$(counter)', value[0])) and \
                self.is_existing(task_completed.replace('$(counter)', value[1])):
            return True
        return False

    def check_task_complete(self, value):
        button = self.find_element(checkbox_task_completed)
        if not button.is_selected():
            button.click()
        return True




