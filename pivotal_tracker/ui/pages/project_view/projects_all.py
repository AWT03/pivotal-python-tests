from core.ui.pages.action_page import ActionPage

project_name_reference = '//a[@class="project_name"][text()="$(project_name)"]'


class ProjectAll(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)

    def project_exists(self, name):
        try:
            self.find_element(project_name_reference.replace('$(project_name)', name))
            return True
        except project_name_reference:
            return False
