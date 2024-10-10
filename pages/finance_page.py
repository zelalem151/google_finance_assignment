from selenium.webdriver.common.by import By
from .base_page import BasePage

class FinancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.google.com/finance/"

    def open_page(self):
        self.driver.get(self.url)

    def verify_title(self, expected_title):
        assert expected_title in self.driver.title, f"Title mismatch: Expected '{expected_title}' but got '{self.driver.title}'"
        assert "Google Finance" in self.driver.title

    def get_stock_symbols(self):
        stocks = self.driver.find_elements(By.CSS_SELECTOR, ".fAThCb .COaKTb")
        stock_symbols = [stock.text.split()[0] for stock in stocks]
        return stock_symbols
