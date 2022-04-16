from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
content = ["Cufcuf snapini vermedi:(", "Gaia cufcufa dc yi gösterdi", "Cynclox r6 da gotumu tasıyo", "Kedhi attıgı memeler ile beni gulduruyo", "C'est ab japonya ya gitcek"]


class Bot:
    def loginpart(self):
        driver.get("https://discord.com/login")
        driver.maximize_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(1)
        user = driver.find_element_by_name("email").send_keys("emirbayraktar_6002@outlook.com")
        password = driver.find_element_by_name("password").send_keys("callback_13579")
        time.sleep(2)
        loginbuton2 = driver.find_element(By.XPATH,
                                          '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(10)
        skip = driver.find_element(By.XPATH,
                                   '//*[@id="app-mount"]/div[5]/div[2]/div/div/div/div[1]/div[2]/button').click()
        time.sleep(1)
        bio = driver.find_element(By.XPATH,
                                  '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[1]/section/div[2]/div[3]/button[3]').click()
        time.sleep(0.2)
        bio2 = driver.find_element(By.XPATH,
                                   '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[3]').click()
        time.sleep(0.2)
        while True:
            read = driver.find_element(By.XPATH,
                                       '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/main/div/div[2]/div/div[1]/div[4]/div[2]/div/textarea').clear()
            time.sleep(0.2)

            for x in content:
                read = driver.find_element(By.XPATH,
                                           '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/main/div/div[2]/div/div[1]/div[4]/div[2]/div/textarea').clear()
                time.sleep(0.2)

                read = driver.find_element(By.XPATH,
                                           '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/main/div/div[2]/div/div[1]/div[4]/div[2]/div/textarea').send_keys(f" {x}")
                time.sleep(0.5)
                readsave = driver.find_element(By.XPATH,
                                               '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/button[2]').click()
                time.sleep(3)



    def bottesting(self):
        bot_testing_part = input("If you did press the q")


p1 = Bot()
p1.loginpart()

