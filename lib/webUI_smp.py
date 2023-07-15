# coding=utf-8
# author: onebear
# datetime: 2023/7/15 15:29
# description: 封装

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from cfg import *
from time import sleep


class SMP_UI:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.wd = webdriver.Chrome(chrome_options=options)
        self.wd.implicitly_wait(10)


    def login(self, username, password):
        self.wd.get(SMP_URL_LOGIN)
        time.sleep(2)  # 手工设置时间，防止登录太快

        if username:
            self.wd.find_element(By.ID, 'username').send_keys(username)
        if password:
            self.wd.find_element(By.ID, 'password').send_keys(password)

        time.sleep(1)
        self.wd.find_element(By.ID, 'loginBtn').click()

smp_ui = SMP_UI()   #直接实例化