from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.task_page import TaskPage

more_options = 'a[href*="/settings"]'
background_div = '.scrim'
story_arrow_element = '[data-type="icebox"] [aria-label="$(story)"] [data-aid="StoryPreviewItem__expander"]'
add_new_task_select = '[data-type="icebox"] [class="tasks full"] [data-aid="TaskAdd"]  span:nth-child(2)'


class ProjectMainPage(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "More": lambda: self.more_settings(),
            "Arrow Story Name Icebox": lambda value: self.click_on_arrow_story_icebox(value),
            "Add a task": lambda: self.click_on_add_a_task()
        }
        self.update_actions(**actions)

    def more_settings(self):
        self.wait_until(background_div)
        self.click(more_options)

    def click_on_arrow_story_icebox(self, value):
        self.wait_until(background_div)
        replaced = story_arrow_element.replace('$(story)', value)
        self.click(replaced)
        return ProjectMainPage(self.get_driver())

    def click_on_add_a_task(self):
        self.click(add_new_task_select)
        return TaskPage(self.get_driver())
