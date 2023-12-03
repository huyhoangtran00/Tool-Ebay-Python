from selenium import webdriver
from tkinter import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gui import ListOfListsApp

login = Tk()
# Gui = Tk()
# hoang = ListOfListsApp(root=Gui)
tk = open("user.txt", "r")
res_true = open("succesfully.txt", "w")
res_false = open("failed.txt", "w")
list = [s.strip() for s in tk.readlines()]
res_err = open("dinh_captcha.txt", "a")
set_thanhcong = set()
set_thatbai = set()
dinh_captcha = set()


Proxy = open("proxy.txt", "r")
PROXY = Proxy.read()


options = Options()
if PROXY != "":
    options.add_argument("--proxy-server=%s" % PROXY)
else:
    pass
# options.add_argument("--incognito")
prefs = {"disk-cache-size": 4096}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)
options.add_extension("ex.crx")
driver = webdriver.Chrome(options=options)
driver.get("https://whoer.net/")


def solve_captcha():
    driver.find_element(By.ID, "captcha_loading")
    print("Captcha is sloving ...........")
    dinh_captcha.add(user_name)
    wait = WebDriverWait(driver, 300)
    crr = driver.current_url
    wait.until(EC.url_changes(crr))
    sleep(1)
    print("Captcha is sloved")
    with open("dinh_captcha.txt", "w") as file:
        file.writelines(k + "\n" for k in dinh_captcha)


def set_check():
    login.destroy()


def run():
    driver.get("https://www.ebay.com/")
    try:
        solve_captcha()
    except:
        pass
    try:
        solve_captcha()
    except:
        pass
    try:
        solve_captcha()
    except:
        pass

    sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
    try:
        solve_captcha()
    except:
        pass
    try:
        solve_captcha()
    except:
        pass
    try:
        solve_captcha()
    except:
        pass
    try:
        solve_captcha()
    except:
        pass
    try:
        solve_captcha()
    except:
        pass
    try:
        solve_captcha()
    except:
        pass
    try:
        solve_captcha()
    except:
        pass
    try:
        sign_in.click()
    except:
        pass
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="userid"]')
        )
    )
    driver.find_element(
        By.XPATH, '//*[@id="userid"]'
    ).send_keys(user_name)
    sleep(1)

    try:
        try:
            solve_captcha()
        except:
            pass

        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located(
                (
                    By.ID,
                    "signin-continue-btn",
                )
            )
        )
        driver.find_element(By.ID, "signin-continue-btn").click()
    except:
        pass

    try:
        sleep(1)
        try:
            solve_captcha()
        except:
            pass
        driver.execute_script('document.querySelector("#fyp-btn").click()')

        try:
            try:
                solve_captcha()
            except:
                pass
            driver.find_element(By.ID, "emailWithCode-btn")
            print(user_name + "->thanh cong\n")
            set_thanhcong.add(user_name)
        except:
            try:
                solve_captcha()
            except:
                pass
            print(user_name + "->loi\n")
            set_thatbai.add(user_name)
    except:
        sleep(1)
        try:
            solve_captcha()
        except:
            pass
        try:
            driver.execute_script(
                'document.querySelector("#need-help-signin-link").click()'
            )
        except:
            pass

    try:
        try:
            solve_captcha()
        except:
            pass
        driver.find_element(By.ID, "fyp-btn").click()
        try:
            try:
                solve_captcha()
            except:
                pass
            driver.find_element(By.ID, "emailWithCode-btn")
            print(user_name + "->thanh cong\n")
            set_thanhcong.add(user_name)
        except:
            try:
                solve_captcha()
            except:
                pass
            print(user_name + "->loi\n")
            set_thatbai.add(user_name)

    except:
        try:
            solve_captcha()
        except:
            pass
        try:
            solve_captcha()
        except:
            pass
        try:
            try:
                solve_captcha()
            except:
                pass
            driver.find_element(By.ID, "emailWithCode-btn")
            print(user_name + "->thanh cong\n")
            set_thanhcong.add(user_name)
        except:
            print(user_name + "->loi\n")
            set_thatbai.add(user_name)


check_submit = False
login.title("RePass")
login.geometry("400x200")
start = Button(
    login, text="Start", command=set_check, width=100, height=100, bg="#FFCC99"
)

start.pack()
login.mainloop()


i = 0
while i < len(list):
    user_name = list[i]
    run()
    with open("succesfully.txt", "w") as file:
        file.writelines(k + "\n" for k in set_thanhcong)
    with open("failed.txt", "w") as file:
        file.writelines(k + "\n" for k in set_thatbai)
    with open("user_dang_chay.txt", "w") as file:
        file.writelines("da xu ly xong :" + user_name)
    i += 1

for i in dinh_captcha:
    res_err.write(i + "\n")
driver.close()

# 869793bb8bcc38a1f5300fcc021f2a67
