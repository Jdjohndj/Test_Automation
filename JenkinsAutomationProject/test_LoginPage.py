import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class TestLogin:
    
    def setup_class(self):
        with open("../Configurations/testdata.json") as file:
            self.configdata = json.load(file)
            # config = json.load(file)

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login(self):
        self.driver.get(self.configdata["url"])
        time.sleep(5)
        self.driver.find_element(By.XPATH, ('//input[@name="username"]')).click()
        self.driver.find_element(By.XPATH, ('//input[@name="username"]')).send_keys(self.configdata["username"])
        self.driver.find_element(By.XPATH, ('//input[@name="password"]')).click()
        self.driver.find_element(By.XPATH, ('//input[@name="password"]')).send_keys(self.configdata["password"])
        self.driver.find_element(By.XPATH, ('//button[@type="submit"]')).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, ('//span[text()="Admin"]')).click()
        self.driver.find_element(By.XPATH, ('(//input[@class="oxd-input oxd-input--active"])[2]')).click
        self.driver.find_element(By.XPATH, ('(//input[@class="oxd-input oxd-input--active"])[2]')).send_keys("Admin")
        self.driver.find_element(By.XPATH, ('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')).click()
        self.driver.find_element(By.XPATH, ('(//span[contains(text(), "Admin")])[1]')).click()
        self.driver.find_element(By.XPATH, ('(//div[@class="oxd-select-text-input"])[2]')).click()
        self.driver.find_element(By.XPATH, ('(//span[contains(text(), "Enabled")])[1]')).click()
        
        time.sleep(10)
        print("test ran successfully")

















# with open ("configurationsfile/loginPage.json") as file:
#     configdata = json.load(file)
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get(configdata["url"])
# driver.fullscreen_window()
# time.sleep(10)
# driver.find_element(By.XPATH, ('//input[@name="username"]')).click()
# driver.find_element(By.XPATH, ('//input[@name="username"]')).send_keys(configdata["username"])
# driver.find_element(By.XPATH, ('//input[@name="password"]')).click()
# driver.find_element(By.XPATH, ('//input[@name="password"]')).send_keys(configdata["password"])
# driver.find_element(By.XPATH, ('//button[@type="submit"]')).click()
# time.sleep(10)
