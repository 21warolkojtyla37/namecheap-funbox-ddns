from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from config import *

driver = webdriver.Chrome()
 
driver.get('http://' + ROUTER_IP)
inp = driver.find_element(By.CLASS_NAME, 'userPw')
inp.send_keys(PASS)
driver.find_element(By.CLASS_NAME, 'log-button').click()
time.sleep(0.5)
driver.get('http://' + ROUTER_IP + '/' + 'advConfigNetworkNatPat.html')
time.sleep(1.5)
x = driver.find_element(By.XPATH, '//span[@id="externalIP"]').text
driver.get(f'https://dynamicdns.park-your-domain.com/update?host={host}&domain={domain}&password={ddns_pass}&ip={x}%27)
