from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=(Service(ChromeDriverManager().install())))
link = "https://www.metacritic.com/movie/vertigo-1958"
browser.get(link)
sleep(5)
gen = browser.find_element(By.CSS_SELECTOR,"div[class='genres']")
print('gen ',gen)
res = gen.text.replace("Genre(s): ",'').split(", ")
print('res ',res)