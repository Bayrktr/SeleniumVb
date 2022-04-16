from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sqlite3 as sql
from datetime import datetime
import locale
import json
from urllib.request import urlopen
import re, os


def findlocale(operation):
    myIP = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(str(urlopen('http://checkip.dyndns.com/').read())).group(
        1)

    url = f'http://ipinfo.io/{myIP}/json'
    response = urlopen(url)
    data = json.load(response)

    return data[operation]


locale.setlocale(locale.LC_ALL, findlocale("country"))


def time_setting(key):
    date = datetime.now()

    date_info = datetime.strftime(date, "%Y"), datetime.strftime(date, "%X"), datetime.strftime(date,
                                                                                                "%A"), datetime.strftime(
        date,
        "%B"), datetime.strftime(
        date, "%d")

    timeInfo = {
        "Year": date_info[0],
        "Hour": date_info[1],
        "Day": date_info[2],
        "Month": date_info[4] + " " + date_info[3]
    }

    # date_msg_info = f"Month: {timeInfo['Month']} {timeInfo['Day']}\nH   our: {timeInfo['Hour']}\nYear: {timeInfo['Year']}"

    return timeInfo[key]


class bot:
    def __init__(self):
        self.veri_list = []
        self.c = 0
        self.y = 0
        self.column_list = ["shipment", "fallowers", "follow_up"]
        self.list_of_new = []
        self.content = []
        self.db_list = []
        self.new_list = []
        self.targetname_list = []
        self.url = 'https://www.instagram.com/'
        self.search = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
        self.run = True

        # print(self.username,self.password,end="\n")

    def select_user(self):
        self.name = input("Kullanıcı adi")
        self.password_1 = input("Şifre ")
        while self.run == True:
            self.targetname = input("Username = ?")
            if self.targetname == "y":
                self.run = False
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
                p1.login()
            else:
                self.targetname_list.append(self.targetname)

    def login(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        time.sleep(3)
        self.driver.get(self.url)
        time.sleep(2)
        name = self.driver.find_element(By.NAME, 'username').send_keys(f"{self.name}")
        time.sleep(0.02)
        passwrd = self.driver.find_element(By.NAME, 'password').send_keys(f"{self.password_1}")
        time.sleep(1)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(3)
        p1.go_to()

    def go_to(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        time.sleep(3)
        p1.go_to_user()

    def go_to_user(self):
        for x in self.targetname_list:
            self.driver.get(f"{self.url}" + str(x) + '/')
            time.sleep(2)
            p1.take_content()

    def take_content(self):
        content = self.driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        self.user_content = soup.find_all("span", attrs={"class": "g47SY"})
        for x in self.user_content:
            self.new_list.append(f'{x.text}')
        p1.press_of_txt()

    def create_bank(self):
        content = self.new_list
        for self.x in self.targetname_list:
            print(self.x)
            hour, minute, day, year, month = time_setting("Hour"), time_setting("Hour")[3:5], time_setting(
                "Day"), time_setting("Year"), time_setting("Month")
            date = str(hour) + str(minute) + " " + str(day) + " " + str(year) + " " + str(month)
            with sql.connect('veribankam.sqlite') as vt:
                im = vt.cursor()
                im.execute(
                    f"CREATE TABLE if not exists {self.x}_content (user TEXT,date TEXT,shipment TEXT,fallowers TEXT,follow_up TEXT)")
                im.execute(f"insert into {self.x}_content values (?,?,?,?,?)",
                           (self.x, date, content[0], content[1], content[2]))
                vt.commit()
                print("Veri tabanına veri girildi...")
            self.veri = [self.x, date, self.new_list[0], self.new_list[1], self.new_list[2]]
        p1.select_datas_test()

    def select_datas_test(self):
        for x in self.targetname_list:
            with sql.connect('veribankam.sqlite') as vt:
                im = vt.cursor()
                im.execute(f"select * from {x}_content")
                content = im.fetchall()
                for y in content:
                    self.list_of_new.append(y)

        print(self.list_of_new)
        p1.go_to_user()

    def press_of_txt(self):
        for x in self.targetname_list:
            with open("{}.txt".format(x), "a+") as ds:
                if os.path.exists(f"{x}.txt"):
                    self.y += 1
                    print("Veri Dosyası mevcut veri giriliyor...")
                    self.veri = " | ".join(self.new_list)
                    hour, minute, day, year, month = time_setting("Hour"), time_setting("Hour")[3:5], time_setting(
                        "Day"), time_setting("Year"), time_setting("Month")
                    date = str(hour) + str(minute) + " " + str(day) + " " + str(year) + " " + str(month)
                    self.veri = str(x) + str(date) + str(self.veri)
                    self.veri = "{} >>> ".format(self.y) + str(self.veri)
                    ds.write(f"{self.veri}\n")
                    print("Basarılı")
                else:
                    print("Dosya Mevcut değil!!!")
        time.sleep(3)
        p1.switch_wrng_shr()

    def switch_wrng_shr(self):
        a = 0
        for x in self.targetname_list:
            a = + 1
            with sql.connect('veribankam.sqlite') as vt:
                im = vt.cursor()
                im.execute('select * from {}_content'.format(x))
                data = im.fetchall()
                if data == "":
                    with sql.connect('veribankam.sqlite') as dm:
                        im = dm.cursor()
                        im.execute(
                            f"CREATE TABLE if not exists {x}_content (user TEXT,date TEXT,shipment TEXT,fallowers TEXT,follow_up TEXT)")
                        im.execute(f"insert into {x}_content values (?,?,?,?,?)",
                                   (x, "0", "0", "0", "0"))
                        dm.commit()

                data = data[len(data) - 1]
                self.veri_list.append(data[2])
                self.veri_list.append(data[3])
                self.veri_list.append(data[4])
                vt.commit()
            print(self.new_list)
            print(self.veri_list)
            print(a)
            if a == 1:
                if self.new_list[0] != self.veri_list[0]:
                    with open("{}_switch_shipment.txt".format(x), "a+") as ds:
                        if os.path.exists("{}_switch_shipment.txt".format(x)):
                            print("Switch dosyası mevcut shipment giriliyor...")
                            if self.new_list[0] > self.veri_list[0]:
                                mesaj = "SHIPMENT +"
                            else:
                                mesaj = "SHIPMENT -"
            if a == 2:
                if self.new_list[1] != self.veri_list[1]:
                    with open("{}_switch_followers.txt".format(x), "a+") as ds:
                        if os.path.exists("{}_switch_shipment.txt".format(x)):
                            print("Switch dosyası mevcut FOLLOWERS giriliyor...")
                            if self.new_list[1] > self.veri_list[1]:
                                mesaj = "FOLLOWERS +"
                            else:
                                mesaj = "FOLLOWERS -"
            if a == 3:
                if self.new_list[2] != self.veri_list[2]:
                    with open("{}_switch_follow_up.txt".format(x), "a+") as ds:
                        if os.path.exists("{}_switch_shipment.txt".format(x)):
                            print("Switch dosyası mevcut FOLLOW_UP giriliyor...")
                            if self.new_list[2] > self.veri_list[2]:
                                mesaj = "FOLLOW_UP +"
                            else:
                                mesaj = "FOLLOW_UP -"
        time.sleep(10)
        p1.create_bank()


if __name__ == "__main__":
    p1 = bot()
    p1.select_user()
