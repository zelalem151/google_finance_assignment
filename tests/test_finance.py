# tests/test_finance.py

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.finance_page import FinancePage

@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--remote-debugging-port=9222")  # Required for some environments

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

def test_compare_stock_symbols(setup):
    driver = setup
    finance_page = FinancePage(driver)

    # Step 1: Open the Google Finance page
    finance_page.open_page()

    # Step 2: Verify the page title
    finance_page.verify_title("Google Finance")

    # Step 3: Retrieve stock symbols from the UI
    ui_stock_symbols = finance_page.get_stock_symbols()
    print("Stock symbols from UI:", ui_stock_symbols)

    # Step 4: Given Test Data
    test_data = ["NFLX", "MSFT", "TSLA"]

    # Step 5: Compare UI data with given test data
    missing_in_ui = [stock for stock in test_data if stock not in ui_stock_symbols]
    extra_in_ui = [stock for stock in ui_stock_symbols if stock not in test_data]

    # Step 6: Output the results
    print(f"Stocks in test data but not in UI: {missing_in_ui}")
    print(f"Stocks in UI but not in test data: {extra_in_ui}")


