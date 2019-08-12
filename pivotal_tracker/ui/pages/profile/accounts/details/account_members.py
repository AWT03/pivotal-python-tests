from core.ui.pages.action_page import ActionPage
from core.ui.pages.element_search import ElementSearch

member_row_owner = '//li[@class="owner"]/ancestor::li[contains(@id, "membership_row")]' \
                   '/div[@class="email ellipsify"][contains(text(), "$(email)")]'


class AccountMembers(ActionPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
        }
        search_elements = {
            "Owner": lambda value: self.is_existing(member_row_owner.replace('$(email)', value))
        }
        self.update_actions(**actions)
        self.update_search_fields(**search_elements)
