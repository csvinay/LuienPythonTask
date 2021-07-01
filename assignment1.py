from selenium import webdriver
from bs4 import BeautifulSoup
import time
from bs4.element import Tag
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

query = input("Enter the company name:")

google_url = "https://www.google.com/search?q="+ query + "&num=" + str(5)
driver.get(google_url)
time.sleep(3)

soup = BeautifulSoup(driver.page_source,'lxml')
result_div = soup.find_all('div', attrs={'class': 'g'})


links = []
for r in result_div:
    # Checks if each element is present, else, raise exception
    try:
        link = r.find('a', href=True)
        # Check to make sure everything is present before appending
        if link != '':
            links.append(link['href'])
    # Next loop if one element is not present
    except Exception as e:
        print(e)
        continue
print("The company website url from google search is:", links[0])