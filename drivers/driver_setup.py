from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverSetup:
    @staticmethod
    def get_driver(browser="chrome"):
        """
        Return a WebDriver instance for the specified browser.

        :param browser: Name of the browser (e.g., "chrome", "firefox", "edge").
        :return: WebDriver instance.
        """
        browser = browser.lower()

        if browser == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service)

        elif browser == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service)

        elif browser == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            return webdriver.Edge(service=service)

        else:
            raise ValueError(f"Browser '{browser}' is not supported. Supported browsers: chrome, firefox, edge")
