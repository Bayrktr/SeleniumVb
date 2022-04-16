from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time,string


driver = webdriver.Chrome(ChromeDriverManager().install())

class bot:
    def __init__(self):
        self.latin = string.ascii_letters
        self.latin = list(self.latin)
        print(self.latin)
        self.mesaj = "latin alfabesi !!!"

    def login(self):
        driver.get("https://web.whatsapp.com/")
        kontrol = input("Devam etmek için y")
        if kontrol == "y":
            p1.go_to_group()
        else:
            print("bitti")

    def go_to_group(self):
        grub_click = driver.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]').click()
        time.sleep(3)
        p1.check_content()

    def check_content(self):
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        self.content = soup.find("div",attrs={"class":"_22Msk"}).text
        print(self.content)
        self.content = list(self.content)
        print(self.content)
        for x in self.content:
            if x not in self.latin:
                print("sorun yok")
            else:
                print("Buldum")
                time.sleep(3)
                p1.sendmessage()
                p1.check_content()

    def sendmessage(self):
        sendmessage = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div').send_keys(f"{self.mesaj}")
        time.sleep(0.5)
        click = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]').click()
        time.sleep(0.5)

if __name__ == "__main__":
    p1 = bot()
    p1.login()