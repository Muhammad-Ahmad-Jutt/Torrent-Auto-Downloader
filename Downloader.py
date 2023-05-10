from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def perform_action(link):
    tabnumber = -1
    driver = webdriver.Firefox()
    driver.get('https://www.google.com')
    for i, element in enumerate(link):
        if i == 0:
            continue  # skip the first iteration
        link1 = "https://www.1377x.to" + element
        driver.switch_to.window(driver.current_window_handle)
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[tabnumber])

        # action in after opening the page
        driver.get(link1)
        button = driver.find_element(By.CLASS_NAME, "dropdown")
        button.click()
        driver.switch_to.window(driver.window_handles[tabnumber])
        sec_button = driver.find_element(By.CLASS_NAME, "flaticon-l7b5578fc3bfed52a6c058caaf05c64d9065edf6e")
        sec_button.click()
        time.sleep(5)

    driver.quit()


url = "https://www.1377x.to/popular-movies-week"
targetlink = "torrent"
text_len = 14
main_page = requests.get(url)
p_page = BeautifulSoup(main_page.content, "html.parser")

sec_links = p_page.find_all("a")
list_1 = []
for link in sec_links:
    plink = link.get("href")
    if len(plink) > 12:
        domain = urlparse(plink).path
        if targetlink in domain:
            list_1.append(domain)
        else:
            print("Did not found the target link")
perform_action(list_1)
