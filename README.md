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

### Running esg_report_search.py
After successfully installing the packages required, refer to line 11 on `esg_report_search.py`. You will need to replace the chromedriverurl to your own chromedriver downloaded location:
```
chromedriverurl = "replace_with_your_chromedriver_downloaded_location"
```
Once you have updated the location, you should be able to run this `.py` file with your desired company and year of reports you would like to collect from. <br>
To change the company, you can enter the stock code on line 28 under the variable `search_content`. For example, if you want to search for 09992: <br>

Replace:
```
search_content = "HKEX_stock_code"
```
To this:
```
search_content = "09992"
```
To change the year, you can enter the year on line 98 under the variable `year`. For example, if you want to search for year 2021 or 2021/22: <br>

Repalce:
```
year_options = ["year"]
```
To this:
```
year_options = ["2021"]
```

### Results
In some cases, the engine may produce multiple responses, which is completely normal. Given the diverse range of variables, such as varying titles in ESG reports, human intervention remains necessary to address specific instances. Nevertheless, this feature significantly enhances time efficiency during task execution. Please kindly notify me of any encountered challenges by submitting an issue ticket in this repository, and I will promptly rectify them.
