from src.webdriver import WebdriverConfiguration
from src.add_remove_elements import AddRemove

webdriver_manager = WebdriverConfiguration()
add_remove_elements = AddRemove(webdriver_manager.driver)
add_remove_elements.get_page()
add_remove_elements.click_on_button_add_element()
add_remove_elements.remove_button_added()