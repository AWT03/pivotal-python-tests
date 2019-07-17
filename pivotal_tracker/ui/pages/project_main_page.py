from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.task_page import TaskPage
from pivotal_tracker.ui.pages.story_creation_page import StoryCreationPage
from pivotal_tracker.ui.pages.project_settings_form import ProjectSettingsForm


more_options = 'a[href*="/settings"]'
background_div = '.scrim'
story_arrow_element = '[data-type="icebox"] [aria-label="$(story)"] [data-aid="StoryPreviewItem__expander"]'
add_new_task_select = '[data-type="icebox"] [class="tasks full"] [data-aid="TaskAdd"]  span:nth-child(2)'
task_description_field = '[data-type="icebox"] [class="tasks full"] div[data-aid="Tasks"] ' \
                         'div[data-aid="TaskShow"] span:nth-child(1) p'
task_description_value_field = '//p[text()="$(task)"]'
add_story_backlog = 'div[id*="panel_backlog"] a[class*="FirstStoryAddButton"]'


class ProjectMainPage(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "More": lambda: self.more_settings(),
            "Story Name Icebox": lambda value: self.click_on_arrow_story_icebox(value),
            "Add a task": lambda: self.click_on_add_a_task(),
            "Mouse Hover Task Description": lambda: self.mouse_over_task_description(),
            "Task Description": lambda value: self.click_on_task_description(value),
            "Add Story": lambda: self.add_story()
        }
        self.update_actions(**actions)

    def more_settings(self):
        self.wait_until(background_div)
        self.click(more_options)
        return ProjectSettingsForm(self._driver)

    def click_on_arrow_story_icebox(self, value):
        self.wait_until(background_div)
        replaced = story_arrow_element.replace('$(story)', value)
        self.click(replaced)
        return ProjectMainPage(self.get_driver())

    def click_on_add_a_task(self):
        self.click(add_new_task_select)
        return TaskPage(self.get_driver())

    def mouse_over_task_description(self):
        self.mouse_hover_element(task_description_field)
        return TaskPage(self.get_driver())

    def click_on_task_description(self, value):
        replaced = task_description_value_field.replace('$(task)', value)
        self.click(replaced)
        return TaskPage(self.get_driver())

    def add_story(self):
        self.wait_until(background_div)
        self.click(add_story_backlog)
        return StoryCreationPage(self._driver)
