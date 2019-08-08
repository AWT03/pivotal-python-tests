from core.ui.pages.action_page import ActionPage
from core.ui.pages.element_search import ElementSearch

current_plan_field = '//span[@class="summary_header"][text()=" $(plan_name)"]'


class AccountPlansBilling(ActionPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
        }
        search_elements = {
            "Current Plan": lambda value: self.is_existing(
                current_plan_field.replace('$(plan_name)', value))
        }
        self.update_actions(**actions)
        self.update_search_fields(**search_elements)
