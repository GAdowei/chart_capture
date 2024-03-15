import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
options = Options()
# Uncomment the next line if you want to run Chrome headlessly (without opening a GUI window)
# options.add_argument("--headless")
options.add_experimental_option('detach', True)

# Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Define the sources and currencies you want to capture
sources = ['BITSTAMP', 'COINBASE', 'BINANCE', 'CRYPTO', 'BITFINEX', 'KRAKEN', 'GEMINI']
currencies = ['BTCUSD', 'ETHUSD', 'SOLUSD']

for source in sources:
    # Get the current working directory
    current_dir = os.getcwd()
    # Create a directory path for the current source
    dir = 'assets/' + source
    path = os.path.join(current_dir, dir)
    # Check if the directory already exists, delete it if it does
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
        except Exception as e:
            print(f"Error removing directory {path}: {e}")
            continue
    try:
        # Create a new directory for the current source
        os.makedirs(path)
    except Exception as e:
        print(f"Error creating directory {path}: {e}")
        continue

    for currency in currencies:
        try:
            # Construct the URL for the current source and currency
            url = 'https://www.tradingview.com/chart/?symbol=' + source + '%3A' + currency
            # Navigate to the URL
            driver.get(url)
            # Maximize the browser window to ensure the chart is fully visible
            driver.maximize_window()
            # Wait 2 seconds to ensure the page has loaded completely
            time.sleep(3)
            # Save a screenshot of the chart
            driver.save_screenshot(path + '/' + currency + '.png')
            print(currency, 'chart by', source, 'captured successfully')
        except Exception as e:
            print(f"Error capturing {currency} chart by {source}: {e}")

# Close the WebDriver
driver.quit()
