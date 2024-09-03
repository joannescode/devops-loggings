from library.logger import LoggerForDevOps
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class AddRemove:
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, driver) -> None:
        self.devops_logs = LoggerForDevOps("logs")
        self.driver = driver

    def get_page(self):
        self.driver.get(self.URL)
        self.devops_logs.logging_info(message="Page requested...")

    def click_on_button_add_element(self):
        button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
        for _ in range(5):
            button.click()
            self.devops_logs.logging_info("Button added.")

    def remove_button_added(self):
        try:
            #all_buttons = WebDriverWait(self.driver, 3).until(
            #    EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manuallp")) # force warning logging
            #)
            
            all_buttons = WebDriverWait(self.driver, 3).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manually"))
            )
            
            self.devops_logs.logging_debug("Buttons founded.")
            for button in all_buttons:
                if button.is_displayed():
                    button.click()
                    self.devops_logs.logging_info("Button removed.")
            
            #all_buttons.click() # force critical logging
        except TimeoutException:
            self.devops_logs.logging_warning(
                "TimeoutException: Element not found and time for located expiration."
            )

        except Exception as e:
            self.devops_logs.logging_critical(f"Exception: An error ocurred.")

