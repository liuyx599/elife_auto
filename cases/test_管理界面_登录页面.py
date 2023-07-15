# coding=utf-8
# author: onebear
# datetime: 2023/7/15 11:43
# description:
import time

import pytest
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
    sleep(1)
    nav = smp_ui.wd.find_element(By.TAG_NAME, 'nav')

    assert nav != []


@pytest.fixture
# 默认function级别，它会在每个测试函数执行前后各执行一次，用来清除可能存在的 alert 弹窗
def clearAlert():
    yield
    try:
        smp_ui.wd.switch_to.alert.accept()
    except Exception as e:
        print(e)


def test_SMP_login_002(clearAlert):
    # 创建WebDriver对象

    # 如果没有配置环境变量，指定webdriver的驱动地址也可以
    # wd = webdriver.Chrome(service=Service(r"d:\software\chromedriver.exe"))

    smp_ui.login(None, 'sdfsdf')

    # 验证是否到达管理页面
    sleep(1)
    alert = smp_ui.wd.switch_to.alert
    assert alert.text == '请输入用户名'


def test_SMP_login_003(clearAlert):

    smp_ui.login('byhy', None)

    # 验证是否到达管理页面
    sleep(1)
    alert = smp_ui.wd.switch_to.alert
    assert alert.text == '请输入密码'



@pytest.mark.parametrize("username, password, expected_alert", [
    ('', '123456', '请输入用户名'),  # 空用户名
    ('', '12345622', '请输入用户名'),  # 空用户名
    ('admin', '', '请输入密码'),  # 空密码
    ('byhy', '', '请输入密码'),  # 空密码
    ('byhy', 'sdsdsd', '登录失败： 用户名或者密码错误'),  # 错误的密码
    ('byhyy', 'sdfsdf', '登录失败： 用户名不存在'),  # 用户名不存在
    ('byh', 'sdfsdf', '登录失败： 用户名不存在')  # 用户名不存在
])
def test_SMP_login_004(username, password, expected_alert, clearAlert):
    # 输入用户名和密码登录
    smp_ui.login(username, password)
    time.sleep(0.5)
    alert = smp_ui.wd.switch_to.alert
    assert alert.text == expected_alert
