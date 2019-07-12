from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage

story_title = 'textarea[name*="story"]'
save_button = 'button[id*="story_close_c211"]'
cancel_button = 'button#story_submit_cancel_c211'


class StoryCreationPage(FormPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "story_title": lambda value: self.set_value(story_title, value)
        }
        actions = {
            "Save": lambda: self.click(save_button),
            "Cancel": lambda: self.click(cancel_button)
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

