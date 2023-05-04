import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)
# driver.set_window_size(1920,1080)
driver.maximize_window()
driver.get('https://outlook.live.com/owa/')
bt_log_in = driver.find_element(By.XPATH, "/html/body/header/div/aside/div/nav/ul/li[2]/a").click()
input_login = driver.find_element(By.NAME, "loginfmt")
input_login.send_keys("dominicpf9@outlook.com")
input_next = driver.find_element(By.ID, "idSIButton9").click()
input_pass = driver.find_element(By.NAME, "passwd")
input_pass.send_keys("rumvt16Mt")
time.sleep(2)
submit = driver.find_element(By.ID, "idSIButton9").click()
time.sleep(2)
no_back = driver.find_element(By.ID, "idBtn_Back").click()
# driver.close()

