coding="utf-8"
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from HTMLTestRunnerNew import HTMLTestRunner
import unittest
class office(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://192.168.0.125:801/")
        time.sleep(5)
    def test_case1(self):
        self.driver.find_element_by_id("tbx_UserName").send_keys("adm")
        self.driver.find_element_by_id("tbx_Password").send_keys("adm")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("ibtLogin").click()
        self.assertEqual(self.driver.find_element_by_link_text("注销").text,"注销",msg="bug")
    def test_case2(self):
        self.driver.find_element_by_id("tbx_UserName").send_keys("")
        self.driver.find_element_by_id("tbx_Password").send_keys("")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("ibtLogin").click()
        self.assertEqual(self.driver.find_element_by_css_selector(".main_box > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(1) > label:nth-child(2)").text, "记住登录", msg="bug")
    def test_case3(self):
        self.driver.find_element_by_id("tbx_UserName").send_keys("adm")
        self.driver.find_element_by_id("tbx_Password").send_keys("")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("ibtLogin").click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_css_selector(".main_box > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(1) > label:nth-child(2)").text,"记住登录", msg="bug")
    def test_case4(self):
        self.driver.find_element_by_id("tbx_UserName").send_keys("")
        self.driver.find_element_by_id("tbx_Password").send_keys("adm")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("ibtLogin").click()
        self.assertEqual(self.driver.find_element_by_css_selector(".main_box > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(1) > label:nth-child(2)").text, "记住登录", msg="bug")
    def test_case5(self):
        self.driver.find_element_by_id("tbx_UserName").send_keys("adm")
        self.driver.find_element_by_id("tbx_Password").send_keys("111")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("ibtLogin").click()
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_css_selector(".main_box > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(1) > label:nth-child(2)").text,"记住登录", msg="bug")
    def test_case6(self):
        self.driver.find_element_by_id("tbx_UserName").send_keys("111")
        self.driver.find_element_by_id("tbx_Password").send_keys("111")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("ibtLogin").click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_css_selector(".main_box > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(1) > label:nth-child(2)").text,"记住登录", msg="bug")

    ########################################
    def tearDown(self):
        self.driver.quit()
#*****************************************
if __name__=="__main__":
    unittest.main()













