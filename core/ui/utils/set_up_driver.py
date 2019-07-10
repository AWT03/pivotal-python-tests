from core.ui.user_interface_connection import UserInterfaceConnection


def set_up_driver(config):
    driver = UserInterfaceConnection(config.get('BROWSER')).get_driver()
    driver.get(config.get('INITIAL_PAGE'))
    driver.implicitly_wait(15)
    driver.maximize_window()
    return driver
