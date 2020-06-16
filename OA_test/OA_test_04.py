coding='utf-8'
#项目名称：OA自动化办公系统测试-待办事务
#测试人员：DLL
#时间：20200605
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
class office (unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://192.168.0.101:801/login.aspx")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("tbx_UserName").send_keys("adm")
        self.driver.find_element_by_id("tbx_Password").send_keys("adm")
        self.driver.find_element_by_id("ibtLogin").click()
        time.sleep(3)
    def test_case1(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[6]/li[3]").click()
        self.driver.switch_to.frame("tab_OaAffairReceive_ifm")
        time.sleep(5)
        self.driver.find_element_by_css_selector("tr.grid_body:nth-child(2) > td:nth-child(9)").click()
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("AffairWork347_ifm")###########
        # self.driver.find_element_by_name("result").click()
        self.driver.find_element_by_css_selector("#opinion").send_keys("同意")
        self.driver.find_element_by_css_selector("#selectClerk").click()
        self.driver.switch_to.frame(1)
        self.driver.find_element_by_id("TreeView1n4CheckBox").click()
        self.driver.find_element_by_id("btn_Ok").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("AffairWork347_ifm")
        self.driver.find_element_by_id("save").click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("tab_OaAffairReceive_ifm")
        self.assertEqual(self.driver.find_element_by_id("Label13").text,"搜索关键字：",msg="bug")
    def test_case2(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[6]/li[3]").click()
        self.driver.switch_to.frame("tab_OaAffairReceive_ifm")
        time.sleep(5)
        self.driver.find_element_by_css_selector("tr.grid_body:nth-child(2) > td:nth-child(9)").click()
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("AffairWork348_ifm")###########
        # self.driver.find_element_by_name("result").click()
        self.driver.find_element_by_css_selector("#opinion").send_keys("同意")
        self.driver.find_element_by_css_selector("#selectClerk").click()
        self.driver.switch_to.frame(1)
        self.driver.find_element_by_id("TreeView1n3CheckBox").click()
        self.driver.find_element_by_id("btn_Ok").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("AffairWork348_ifm")
        self.driver.find_element_by_id("save").click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("tab_OaAffairReceive_ifm")
        self.assertEqual(self.driver.find_element_by_id("Label13").text,"搜索关键字：",msg="bug")
    def test_case3(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[6]/li[3]").click()
        self.driver.switch_to.frame("tab_OaAffairReceive_ifm")
        time.sleep(5)
        self.driver.find_element_by_css_selector("tr.grid_body:nth-child(2) > td:nth-child(9)").click()
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("AffairWork349_ifm")
        self.driver.find_element_by_id("save").click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("tab_OaAffairReceive_ifm")
        self.assertEqual(self.driver.find_element_by_id("Label13").text, "搜索关键字：", msg="bug")
    def test_case4(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/ul[6]/li[3]").click()
        self.driver.switch_to.frame("tab_OaAffairReceive_ifm")
        time.sleep(5)
        self.driver.find_element_by_css_selector("tr.grid_body:nth-child(2) > td:nth-child(9)").click()
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("AffairWork349_ifm")
        self.driver.find_element_by_css_selector("#result2 > input:nth-child(1)").click()
        self.driver.find_element_by_id("opinion").send_keys("不同意")
        self.driver.find_element_by_id("save").click()
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("tab_OaAffairReceive_ifm")
        self.assertEqual(self.driver.find_element_by_css_selector("tr.grid_body:nth-child(2) > td:nth-child(5)").text,"【退回】主管领导审批",msg="bug")
    def tearDown(self):
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.quit()
if __name__=="__main__":
    unittest.main()
















