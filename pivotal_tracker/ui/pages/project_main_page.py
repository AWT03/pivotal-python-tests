from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.story_creation_page import StoryCreationPage
from pivotal_tracker.ui.pages.project_settings_form import ProjectSettingsForm

more_options = 'a[href*="/settings"]'
background_div = '.scrim'
add_story_backlog = 'div[id*="panel_backlog"] a[class*="FirstStoryAddButton"]'


class ProjectMainPage(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "More": lambda: self.more_settings(),
            "Add Story": lambda: self.add_story()
        }
        self.update_actions(**actions)

    def more_settings(self):
        self.wait_until(background_div)
        self.click(more_options)
        return ProjectSettingsForm(self._driver)

    def add_story(self):
        self.wait_until(background_div)
        self.click(add_story_backlog)
        return StoryCreationPage(self._driver)
