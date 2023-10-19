from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize Selenium WebDriver with Chrome
chromedriverurl = "replace_with_your_chromedriver_downloaded_location"
service = Service(chromedriverurl)
driver = webdriver.Chrome(service=service)

# Open the HKEX website
driver.get("https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=en")
time.sleep(1)

#accept cookies
btn1 = driver.find_element(by=By.ID,value="onetrust-accept-btn-handler")
btn1.click()
time.sleep(1)

# Find the search box
search_box = driver.find_element(by=By.ID,value="searchStockCode")

# Find and fill in the search box
search_content = "HKEX_stock_code"
search_box.send_keys(search_content)
time.sleep(3)

# Select the first option from the autocomplete list
driver.find_element(by=By.CLASS_NAME,value="autocomplete-suggestion.narrow").click()

# Find the Headline box
headline_box = driver.find_element(by=By.ID,value="tier1-select").click()
time.sleep(1)

# Select the Headline Category option in the dropdown list
driver.find_element(by=By.CSS_SELECTOR,value='div[data-value="rbAfter2006"]').click()
time.sleep(1)

# Find Document Type box
document_box = driver.find_element(by=By.ID,value="rbAfter2006").click()
time.sleep(1)

# Click on "Financial Statements/ESG Information"
financial_statements_dropdown = driver.find_element(By.XPATH, '//a[contains(text(), "Financial Statements/ESG Information")]')
financial_statements_dropdown.click()
time.sleep(1)

# Find all elements containing "ALL"
all_options = driver.find_elements(By.XPATH, '//a[contains(text(), "ALL")]')
time.sleep(1)

# Iterate through the elements and click the first one that corresponds to "ALL"
for option in all_options[::-1]:
    # print(option.text)
    if "ALL" in option.text:
        option.click()
        break
time.sleep(1)

# Find and click the search button
search_button = driver.find_element(By.CLASS_NAME, "filter__btn-applyFilters-js")
search_button.click()
time.sleep(1)

# # Generate all results across multiple pages (uncomment if needed)
# while True:
#     try:
#         load_more_button = driver.find_element(By.CLASS_NAME, "component-loadmore__link")
#         load_more_button.click()
#         time.sleep(1)
#     except Exception as e:
#         break

doc_links = driver.find_elements(By.XPATH, "//div[@class='doc-link']/a")

# Function to clean titles
def clean_title(title):
    return title.lower().replace(" ", "")

# list of acceptable titles
titles = [
    clean_title("Environmental, Social and Governance"),
    clean_title("Environmental, Social & Governance"),
    clean_title("Environmental, Social, and Governance"),
    clean_title("Environmental, Society and Governance"),
    clean_title("ESG Report"),
    clean_title("Sustainability Report"),
    clean_title("Corporate Social Responsibility"),
    clean_title("CSR Report"),
    clean_title("Social Responsibility Report"),
    clean_title("Annual Report")
]

year = ["year"]

# Loop through doc links
for doc_link in doc_links:
    report = clean_title(doc_link.text)

    # Check if report title matches any ESG-related titles
    if any(title in report for title in titles) and any(year in report for year_option in year):
        print(doc_link.text)  # doc name
        print(doc_link.get_attribute("href"))  # doc link

driver.quit()
