from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

headers = {}
headers[
    "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

driver = webdriver.Chrome(ChromeDriverManager().install())


class Bot:
    def login(self):
        driver.get("https://discord.com/login")
        driver.maximize_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(1)
        user = driver.find_element_by_name("email").send_keys("emirbayraktar2006@hotmail.com")
        password = driver.find_element_by_name("password").send_keys("hidragrogi_3162")
        time.sleep(2)
        loginbuton2 = driver.find_element(By.XPATH,
                                          '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()
        time.sleep(10)
        skip = driver.find_element(By.XPATH,
                                   '//*[@id="app-mount"]/div[5]/div[2]/div/div/div/div[1]/div[2]/button').click()
        time.sleep(1)
        serverget = driver.find_element(By.XPATH,
                                        '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[2]/div[2]/div/div').click()
        time.sleep(0.5)

    def content(self):
        veri = driver.page_source
        soup = BeautifulSoup(veri, "html.parser")
        time.sleep(3)
        try:
            self.user_number = soup.find("div", attrs={"class": "channelName-2YrOjO"}).text

            bio = driver.find_element(By.XPATH,
                                      '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[1]/section/div[2]/div[3]/button[3]').click()
            time.sleep(0.2)
            bio2 = driver.find_element(By.XPATH,
                                       '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[3]').click()
            time.sleep(0.2)
            read = driver.find_element(By.XPATH,
                                       '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/main/div/div[2]/div/div[1]/div[4]/div[2]/div/textarea').clear()
            content_press = driver.find_element(By.XPATH,
                                                '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/main/div/div[2]/div/div[1]/div[4]/div[2]/div/textarea').send_keys(
                self.user_number)
            readsave = driver.find_element(By.XPATH,
                                           '//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/button[2]').click()
            time.sleep(0.5)
            esc = driver.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]').click()
            time.sleep(2)

        except:
            print("Veri Bulunamıyor")

    def start(self):
        p1 = Bot()
        p1.content()
        time.sleep(1)


p = Bot()
p.login()
while True:
    p.start()

