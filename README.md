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
search_content = "09992" <-- to this
```
To change the year, you can enter the year(s) on line 56 and 57 under the variable `year` and `year_`. For example, if you want to search for year 2021 or 2021/22: <br>

Repalce:
```
year = "year"
year_ = "year/year"
```
To this:
```
year = "2021"
year_ = "2021/22"
```
The reason why we require to put 2 versions of years is because companies have different report cycles, where some will report from January to December, and some will report in the middle of one year till the middle of the next year, which is why if we want to focus on collecting reports from year 2021, we want both 2021 and 2021/22 (for 2022, it will be 2022 and 2022/23...)

### Results
Sometimes, the engine might generate both the annual report and an esg report, and that is completely normal. While we can't completely eliminate out to return just the esg report because of difference variances, this should help greatly in terms of time efficiency when performing this task. Please let me know if you encounter any issues by submitting a git issue on this repository and I will fix it ASAP.
