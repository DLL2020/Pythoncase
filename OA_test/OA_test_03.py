coding='utf-8'
#项目名称：OA自动化办公系统测试-新建事务
#测试人员：DLL
#时间：20200604
import time
from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
class oiffice (unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://192.168.0.122:808/login.aspx")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("tbx_UserName").send_keys("adm")
        self.driver.find_element_by_id("tbx_Password").send_keys("adm")
        self.driver.find_element_by_id("ibtLogin").click()
        time.sleep(3)
    def test_case1(self):
        self.driver.find_element_by_css_selector(".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(1)").click()
        self.driver.switch_to.frame("tab_OaAffairPost_ifm")
        Select(self.driver.find_element_by_id("kind")).select_by_index(4)
        self.driver.find_element_by_id("subject").send_keys("新建费用报销单")
        self.driver.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("2020-06-04")
        self.driver.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6) > input:nth-child(1)").send_keys("6")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)").send_keys("差旅报销")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3) > input:nth-child(1)").send_keys("3000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > input:nth-child(1)").send_keys("设备采购")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(3) > input:nth-child(1)").send_keys("20000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(3) > input:nth-child(1)").send_keys("23000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("领导已同意")
        self.driver.find_element_by_id("upLocFile").send_keys("C:\\Users\\Administrator\\Desktop\\自动化作业.txt")
        self.driver.find_element_by_id("url").send_keys("简单")
        time.sleep(5)
        self.driver.find_element_by_id("save").click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector(".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(2)").click()
        time.sleep(5)
        self.driver.switch_to.frame("tab_OaAffairList_ifm")
        self.assertEqual(self.driver.find_element_by_css_selector("tr.grid_body:nth-child(2) > td:nth-child(3)").text,"新建费用报销单",msg="bug")
    def test_case2(self):
        self.driver.find_element_by_css_selector(".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(1)").click()
        self.driver.switch_to.frame("tab_OaAffairPost_ifm")
        Select(self.driver.find_element_by_id("kind")).select_by_index(4)
        self.driver.find_element_by_id("subject").send_keys("")
        self.driver.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("2020-06-04")
        self.driver.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6) > input:nth-child(1)").send_keys("6")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)").send_keys("差旅报销")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3) > input:nth-child(1)").send_keys("3000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > input:nth-child(1)").send_keys("设备采购")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(3) > input:nth-child(1)").send_keys("20000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(3) > input:nth-child(1)").send_keys("23000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("领导已同意")
        self.driver.find_element_by_id("upLocFile").send_keys("C:\\Users\\Administrator\\Desktop\\自动化作业.txt")
        self.driver.find_element_by_id("url").send_keys("简单")
        time.sleep(5)
        self.driver.find_element_by_id("save").click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_css_selector("body > div:nth-child(3)").text,"◆\n◆\n!请填写此字段。",msg="bug")
    def test_case3(self):
        self.driver.find_element_by_css_selector(".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(1)").click()
        self.driver.switch_to.frame("tab_OaAffairPost_ifm")
        Select(self.driver.find_element_by_id("kind")).select_by_index(4)
        self.driver.find_element_by_id("subject").send_keys("新建费用报销单")
        self.driver.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("2020-06-04")
        self.driver.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6) > input:nth-child(1)").send_keys("")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)").send_keys("差旅报销")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3) > input:nth-child(1)").send_keys("3000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > input:nth-child(1)").send_keys("设备采购")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(3) > input:nth-child(1)").send_keys("20000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(3) > input:nth-child(1)").send_keys("23000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("领导已同意")
        self.driver.find_element_by_id("upLocFile").send_keys("C:\\Users\\Administrator\\Desktop\\自动化作业.txt")
        self.driver.find_element_by_id("url").send_keys("简单")
        time.sleep(5)
        self.driver.find_element_by_id("save").click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_css_selector("body > div:nth-child(3)").text,"◆\n◆\n!请填写此字段。",msg="bug")
    def test_case4(self):
        self.driver.find_element_by_css_selector(".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(1)").click()
        self.driver.switch_to.frame("tab_OaAffairPost_ifm")
        Select(self.driver.find_element_by_id("kind")).select_by_index(4)
        self.driver.find_element_by_id("subject").send_keys("新建费用报销单")
        self.driver.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("2020-06-04")
        self.driver.find_element_by_css_selector("#body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6) > input:nth-child(1)").send_keys("6")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)").send_keys("差旅报销")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3) > input:nth-child(1)").send_keys("")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > input:nth-child(1)").send_keys("设备采购")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(3) > input:nth-child(1)").send_keys("20000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(3) > input:nth-child(1)").send_keys("23000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("领导已同意")
        self.driver.find_element_by_id("upLocFile").send_keys("C:\\Users\\Administrator\\Desktop\\自动化作业.txt")
        self.driver.find_element_by_id("url").send_keys("简单")
        time.sleep(5)
        self.driver.find_element_by_id("save").click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_css_selector("body > div:nth-child(3)").text,"◆\n◆\n!请填写此字段。",msg="bug")
    def test_case5(self):
        self.driver.find_element_by_css_selector(".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(1)").click()
        self.driver.switch_to.frame("tab_OaAffairPost_ifm")
        Select(self.driver.find_element_by_id("kind")).select_by_index(5)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("subject").send_keys("新增立项申请单")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)").send_keys("新型氧-甲烷火箭发动机研发项目")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > textarea:nth-child(1)").send_keys("保密")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(4) > input:nth-child(1)").send_keys("dll")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > input:nth-child(1)").send_keys("1000000")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(4) > input:nth-child(1)").send_keys("2020-06-05")
        self.driver.find_element_by_css_selector("#upLocFile").send_keys("C:\\Users\\Administrator\\Desktop\\Python知识点.docx")
        time.sleep(10)
        self.driver.find_element_by_id("save").click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector(
            ".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(2)").click()
        time.sleep(5)
        self.driver.switch_to.frame("tab_OaAffairList_ifm")
        self.assertEqual(self.driver.find_element_by_css_selector("tr.grid_body:nth-child(2) > td:nth-child(3)").text,
                         "新增立项申请单", msg="bug")
    def test_case6(self):
        self.driver.find_element_by_css_selector(
            ".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(1)").click()
        self.driver.switch_to.frame("tab_OaAffairPost_ifm")
        Select(self.driver.find_element_by_id("kind")).select_by_index(5)
        time.sleep(5)
        self.driver.find_element_by_id("subject").send_keys("")
        self.driver.find_element_by_css_selector(
            "#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)").send_keys(
            "新型氧-甲烷火箭发动机研发项目")
        self.driver.find_element_by_css_selector(
            "#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > textarea:nth-child(1)").send_keys(
            "保密")
        self.driver.find_element_by_css_selector(
            "#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(4) > input:nth-child(1)").send_keys(
            "dll")
        self.driver.find_element_by_css_selector(
            "#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > input:nth-child(1)").send_keys(
            "1000000")
        self.driver.find_element_by_css_selector(
            "#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(4) > input:nth-child(1)").send_keys(
            "2020-06-04")
        time.sleep(3)
        self.driver.find_element_by_id("upLocFile").send_keys("C:\\Users\\Administrator\\Desktop\\Python知识点.docx")
        time.sleep(5)
        self.driver.find_element_by_id("save").click()
        self.assertEqual(self.driver.find_element_by_css_selector("body > div:nth-child(3)").text,"◆\n◆\n!请填写此字段。",msg="bug")
    def test_case7(self):
        self.driver.find_element_by_css_selector(".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(1)").click()
        self.driver.switch_to.frame("tab_OaAffairPost_ifm")
        Select(self.driver.find_element_by_id("kind")).select_by_index(6)
        time.sleep(5)
        self.driver.find_element_by_id("subject").send_keys("新建请假单")
        # self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)").clear()
        # self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)").send_keys("dll")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(6) > input:nth-child(1)").send_keys("测试员")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)").send_keys("5")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4) > input:nth-child(1)").send_keys("2020-06-05")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6) > input:nth-child(1)").send_keys("2020-06-11")
        self.driver.find_element_by_css_selector("#body > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > textarea:nth-child(1)").send_keys("世界那么大 我想去走走")
        self.driver.find_element_by_id("url").send_keys("23333")
        time.sleep(5)
        self.driver.find_element_by_id("save").click()
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector(".tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(2)").click()
        self.driver.switch_to.frame("tab_OaAffairList_ifm")
        self.assertEqual(self.driver.find_element_by_css_selector("tr.grid_body:nth-child(2) > td:nth-child(3)").text,"新建请假单",msg="bug")

    def tearDown(self):
        self.driver.switch_to.default_content()
        self.driver.quit()
if __name__=="__main__":
    unittest.main()











