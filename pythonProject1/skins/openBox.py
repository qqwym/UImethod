import unittest

import random
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains #鼠标操作包


class OpenBox(unittest.TestCase):
    def __init__(self,web,name,password):
        self.web = web
        self.name = name
        self.password = password
        self.driver = webdriver.Chrome()
        self.url = "https://"+web+"/boxhome/"
        self.driver.set_window_size(2000, 1200)
        self.driver.get(self.url)
        sleep(2)


    def login(self):#登陆
        # sleep(5)
        # self.driver.find_element_by_xpath("//div[@class='log-btns']").click()
        # self.driver.find_element_by_xpath("//div[@class='log-btns']/span").click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                    "//div[@class='log-btns']/span[text()='登陆']"))).click()
        # self.driver.switch_to_alert()
        # sleep(3)
        # c1 = self.driver.find_elements_by_xpath("//div[@class='np-group']/input")
        sleep(2)  # 弹窗出现后，使页面等待2S
        login_username = self.driver.find_element_by_xpath('//*[@type="text"]')
        login_username.click()
        login_username.send_keys(self.name)
        login_passwork = self.driver.find_element_by_xpath('//*[@type="password"]')
        login_passwork.click()
        login_passwork.send_keys(self.password)
        checks = self.driver.find_elements_by_xpath("//*[@type='checkbox']")#86
        for i in checks:
            i.click()
        self.driver.find_element_by_xpath('//*[@class="btn login btn-touch"]').click()  # 登陆按钮

    def cutGame(self,num):#选择游戏
        #num  1：开箱 2：追梦 3：斗箱 4：全民挑战 5：拆弹 6：roll房 7：商城 8：背包 9：邀请 10：充值 11：会员福利
        items = self.driver.find_elements_by_xpath("//*[@class='menu-list']/div[@class='menu-item']")#后面几个（背包、邀请、充值、会员福利）需要登录状态
        x = 1
        for i in items:
            if x == num:
                i.click()
                break
            x = x+1

    def appointBox(self,boxid):#指定开箱
        url = self.url+boxid
        self.driver.get(url)
        self.login()
        sleep(2)
        boxnums = self.driver.find_elements_by_xpath("//div[@class='select-submit']/div")
        s = 0
        x = random.randint(1, 4)  # 随机获得开箱次数
        for i in boxnums:  # 选择开箱次数
            if s == x:
                i.click()
                break
            s = s + 1
        # self.driver.find_element_by_xpath("//*[@class='btn-group']").click()#动画按钮
        # self.driver.find_element_by_xpath("//*[@class='text-title']").click()#返回按钮
        self.driver.find_element_by_xpath("//div[@class='button-open']").click()  # 开箱按钮
        sleep(10)
        # a = self.driver.find_elements_by_xpath("//*[@class='result-item-footer']")#获得单开的放入背包与回收按钮
        # for i in a:
        #     i.click()
        # self.driver.find_element_by_xpath("//*[@class='all-sell']").click()#全部放入背包
        # self.driver.find_element_by_xpath("//*[@class='all-back']").click()#全部回收


    def openBox(self,num):#开箱
        self.cutGame(1)
        s = 0
        # js = "document.getElementById('id').scrollTop=1000000"
        # self.driver.execute_script(js)
        sleep(2)
        box = self.driver.find_elements_by_xpath("//*[@class='bg-buy-item']") #拿到箱子列表
        for i in box:#进入箱子详情
            if num == s:
                ActionChains(self.driver).move_to_element(i).perform()
                i.click()
                break
            s = s+1
        sleep(2)
        boxnums = self.driver.find_elements_by_xpath("//div[@class='select-submit']/div")
        s = 0
        x = random.randint(1, 4)#随机获得开箱次数
        for i in boxnums:#选择开箱次数
            if s == x:
                i.click()
                break
            s = s+1
        # self.driver.find_element_by_xpath("//*[@class='btn-group']").click()#动画按钮
        # self.driver.find_element_by_xpath("//*[@class='text-title']").click()#返回按钮
        self.driver.find_element_by_xpath("//div[@class='button-open']").click()#开箱按钮
        sleep(10)
        # a = self.driver.find_elements_by_xpath("//*[@class='result-item-footer']")#获得单开的放入背包与回收按钮
        # for i in a:
        #     i.click()
        # self.driver.find_element_by_xpath("//*[@class='all-sell']").click()#全部放入背包
        # self.driver.find_element_by_xpath("//*[@class='all-back']").click()#全部回收


    def lucky(self,num):#追梦
        self.cutGame(2)
        sleep(2)
        lucky_item = self.driver.find_elements_by_xpath("//*[@class='dream-tab']/div")#拿到追梦标签
        x = 0
        for i in lucky_item:
            if x == num:
                i.click()
                break
            x = x+1
        lucky_goods = self.driver.find_elements_by_xpath("//*[@class='shop-content']/div")#拿到追梦物品
        x = 0
        for i in lucky_goods:
            if x == 2:
                i.click()
                break
            x = x + 1
        # self.driver.find_element_by_xpath("//*[@class='btn-group']")  # 动画按钮
        self.driver.find_element_by_xpath("//button[@class='dream-btn']").click()#追梦按钮
        sleep(10)
        # self.driver.find_element_by_xpath("//*[@class='all-back']").click()#回收按钮
        # self.driver.find_element_by_xpath("//*[@class='all-sell']").click()#放入背包

    def challenge(self):#全民挑战
        sleep(2)
        challenge = self.driver.find_elements_by_xpath("//*[@class='box_list']/div[@class='sc-pNWdM fqjbnq']")
        x = 1
        num = 2
        for i in challenge:
            if x == num:
                i.click()
                break
            x = x + 1
        sleep(2)
        self.driver.find_element_by_xpath("//*[@class='start_challenge btn-touch']").click()  # 开始挑战和继续挑战
        try:
            a = self.driver.find_element_by_xpath("//*[@class='inner_content']")
            if x == 1:
                self.driver.find_element_by_xpath("//*[@class='putinback btn-touch']").click()  # 放入背包
            else:
                self.driver.find_element_by_xpath("//*[@class='recycle btn-touch']").click()  # 回收
        except:
            if x == 1:
                self.driver.find_element_by_xpath("//*[@class='exit btn-touch']").click()  # 继续挑战
            else:
                self.driver.find_element_by_xpath("//*[@class='recycle btn-touch']").click()  # 执意退出
                sleep(2)
                self.driver.find_element_by_xpath("//*[@class='exit btn-touch']").click()  # 退出挑战并领取奖励
                if x == 1:
                    self.driver.find_element_by_xpath("//[@class='putinback btn-touch']").click()  # 放入背包
                else:
                    self.driver.find_element_by_xpath("//[@class='recycle btn-touch']").click()  # 回收











