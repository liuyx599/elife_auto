# coding=utf-8
# author: onebear
# datetime: 2023/7/15 11:43
# description:
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from cfg import *
from time import sleep

from lib.webUI_smp import smp_ui  # 直接import 实例化好的对象，这样就多个实例共享一个driver




def test_SMP_login_001():

    # 创建WebDriver对象

    # 如果没有配置环境变量，指定webdriver的驱动地址也可以
    # wd = webdriver.Chrome(service=Service(r"d:\software\chromedriver.exe"))
    smp_ui.login('byhy', 'sdfsdf')

    # 验证是否到达管理页面
    nav = smp_ui.wd.find_element(By.TAG_NAME, 'nav')

    assert nav !=[]

def test_SMP_login_002():
    # 创建WebDriver对象

    # 如果没有配置环境变量，指定webdriver的驱动地址也可以
    # wd = webdriver.Chrome(service=Service(r"d:\software\chromedriver.exe"))

    smp_ui.login('', 'sdfsdf')

    # 验证是否到达管理页面
    alert = smp_ui.wd.switch_to.alert
    assert alert.text == '请输入用户名'

    alert.accept()

