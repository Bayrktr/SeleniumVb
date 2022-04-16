from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time, string

driver = webdriver.Chrome(ChromeDriverManager().install())


class bot:
    def __init__(self):
        self.latin = string.ascii_letters
        self.latin = list(self.latin)
        print(self.latin)
        self.mesaj = "KEEEESSSSS !!!"

    def login(self):
        driver.get("https://web.whatsapp.com/")
        kontrol = input("Devam etmek için y")
        if kontrol == "y":
            p1.go_to_group()
        else:
            print("bitti")

    def go_to_group(self):
        time.sleep(3)
        grub_click = driver.find_element(By.XPATH,
                                         '//*[@id="pane-side"]/div[2]/div/div/div[4]/div/div/div[2]').click()
        time.sleep(3)
        p1.sendmessage()

    def sendmessage(self):
        time.sleep(3)
        while True:
            sendmessage = driver.find_element(By.XPATH,
                                              '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(
                f"{self.mesaj}")
            time.sleep(0.5)
            click = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
            time.sleep(0.2)


if __name__ == "__main__":
    p1 = bot()
    p1.login()
