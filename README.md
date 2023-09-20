# ESG Report Engine
A web scraper that generates a list of ESG reports according to the stock exchange code and specific year

## Getting Started
### Install required packages
First, please make sure you have ***python*** and ***pip*** installed in your system. Then, please install the packages below in order to run the engine successfully:
```
pip install selenium
pip install beautifulsoup4
```
Next, we will have to install ***chromedriver***. Check your current Chrome version:<br>
For version 115 or newer: https://googlechromelabs.github.io/chrome-for-testing/ <br>
For older versions: https://chromedriver.chromium.org/downloads

### Making edits on .py file
After successfully installing the packages required, refer to line 11 on esg_report_search.py. You will need to replace the chromedriverurl to your own chromedriver downloaded location:
```
chromedriverurl = "replace_with_your_chromedriver_downloaded_location"
```
