from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)
driver.get('https://www.google.com/?hl=en')
input_google = driver.find_element("name","q")
input_google.send_keys("hello qa")
input_google.send_keys(Keys.RETURN)
assert "hello qa - Google Search" in driver.title
# driver.close()
