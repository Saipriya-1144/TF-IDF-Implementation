from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# Define the chromedriver service
s = Service('chromedriver.exe')

# Instantiate the webdriver
driver = webdriver.Chrome(service=s)

page_URL = "https://leetcode.com/problemset/all/?page="


def get_a_tags(url):
    # load the URL in the browser
    driver.get(url)

    time.sleep(7)

    links = driver.find_elements(By.TAG_NAME, "a")
    ans = []

    for i in links:
        try:
            # Check if '/problems/' is in the href of the 'a' element
            if "/problems/" in i.get_attribute("href"):
                # If it is, append it to the list of links
                ans.append(i.get_attribute("href"))
        except:
            pass

    ans = list(set(ans))

    return ans


my_ans = []

for i in range(1, 55):

    my_ans += (get_a_tags(page_URL+str(i)))

my_ans = list(set(my_ans))


with open('lc.txt', 'a') as f:
    for j in my_ans:
        f.write(j+'\n')

print(len(my_ans))
driver.quit()
