from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize Selenium WebDriver with Chrome
chromedriverurl = "/Users/justinphen/Downloads/chromedriver-mac-x64/chromedriver"
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
search_content = "00630"
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

# Select Financial Statements/ESG Information box
driver.find_element(by=By.CSS_SELECTOR,value='li[data-value="40000"]').click()
time.sleep(1)

# Select option "All"
script = """
    var element = document.querySelector('div.droplist-group.droplist-submenu.level2 ul.droplist-items li[data-value="40400"] a');
    element.click();
    """
driver.execute_script(script)
time.sleep(1)

# Find and click the search button
search_button = driver.find_element(By.CLASS_NAME, "filter__btn-applyFilters-js")
search_button.click()
time.sleep(3)

# Generate all results across multiple pages
# while True:
#     try:
#         load_more_button = driver.find_element(By.CLASS_NAME, "component-loadmore__link")
#         load_more_button.click()
#         time.sleep(3)
#     except Exception as e:
#         break

# Get doc links
doc_links = driver.find_elements(By.XPATH, "//div[@class='doc-link']/a")
esg_title = "Environmental, Social and Governance".lower().replace(" ", "")
esg_b_title = "Environmental, Social & Governance".lower().replace(" ", "")
esg_c_title = "ESG Report".lower().replace(" ", "")
annual_title = "Annual Report".lower().replace(" ", "")
sus_title = "Sustainability Report".lower().replace(" ", "")
year = "2021"
year_ = "2021/22"
for doc_link in doc_links:
    report = doc_link.text.lower().replace(" ", "")
    if (esg_title in report or annual_title in report \
        or sus_title in report or esg_b_title in report or esg_c_title in report) and \
        (year in report or year_ in report): # filtering
        print(doc_link.text) # doc name
        print(doc_link.get_attribute("href")) # doc link

driver.quit()
