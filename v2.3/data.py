from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from tkinter import *
from capmonster_python import HCaptchaTask
from tkinter import *


tk = open("user.txt", "r")
res_true = open("succesfully.txt", "w")
res_false = open("failed.txt", "w")
list = [s.strip() for s in tk.readlines()]


def solve():
    capmonster = HCaptchaTask("869793bb8bcc38a1f5300fcc021f2a67")
    task_id = capmonster.create_task("website_url", "website_key")
    result = capmonster.join_task_result(task_id)
    print(result.get("gRecaptchaResponse"))


Proxy = open("proxy.txt", "r")
PROXY = Proxy.read()


options = Options()
# PROXY = "192.168.0.104:30184"
options.add_argument("--proxy-server=%s" % PROXY)

prefs = {"disk-cache-size": 4096}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)
options.add_extension("ex.crx")
driver = webdriver.Chrome(options=options)
driver.get("https://github.com/")
