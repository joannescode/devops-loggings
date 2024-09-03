from selenium import webdriver
from library.logger import LoggerForDevOps

class WebdriverConfiguration():
    def __init__(self) -> None:
        self.devops_logs = LoggerForDevOps("logs")
        self.driver = None
        self.instance_webdriver()
        
    def instance_webdriver(self):
        configurations = webdriver.EdgeOptions()
        configurations.add_argument("--start-maximized")
        configurations.add_argument("--headless")
        configurations.add_argument("--incognito")
        self.driver = webdriver.Edge(options=configurations)
        self.devops_logs.logging_info(message="Webdriver Initiated...")