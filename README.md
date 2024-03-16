Chart Screenshot Capturer

This Python script automates the process of capturing screenshots of financial charts from TradingView for a predefined list of sources and currencies. It's designed to assist in quickly gathering visual data for analysis or AI vision.

Installation
Before running the script, ensure you have Python installed on your system. This script requires the following Python libraries:

selenium
webdriver_manager
shutil (standard Python library)
os (standard Python library)
time (standard Python library)

You can install the required libraries (except the standard libraries) using pip:

pip install selenium webdriver_manager

Usage
To use the script, simply run it with Python:

python chart_screenshot_capturer.py

Headless Mode
By default, the script runs in a GUI mode where the browser window is visible. If you prefer to run it in headless mode (without displaying the browser window), uncomment the --headless flag in the script:

options.add_argument("--headless")

Customizing Sources and Currencies
The script is preconfigured with a set of sources and tickers:

sources = ['BITSTAMP', 'COINBASE', 'BINANCE', 'CRYPTO', 'BITFINEX', 'KRAKEN', 'GEMINI']
tickers = ['BTCUSD', 'ETHUSD', 'SOLUSD']

You can easily modify this list by adding new sources (e.g., NASDAQ) and tickers (e.g., TSLA) to capture different charts. Ensure to keep the base TradingView URL constant and follow the URL structure for new sources and tickers:

url = base_url' + source + '%3A' + ticker

Assets Folder
The script automatically creates an assets folder in the current working directory, organized by source, to save the captured screenshots. This folder is recreated on each run, so there's no need to delete it manually before rerunning the script. This ensures you always have the latest screenshots without old data interference.

Contributing
Contributions to the script are welcome! Whether it's adding new features, improving the documentation, or reporting issues, your feedback is valuable.
