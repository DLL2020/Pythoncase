coding='utf-8'
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
class office(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://192.168.0.125:801/Login.aspx")
        time.sleep(5)
        self.driver.find_element_by_id("tbx_UserName").send_keys("adm")
        self.driver.find_element_by_id("tbx_Password").send_keys("adm")
        self.driver.find_element_by_id("ibtLogin").click()
        time.sleep(3)
    def test_case1(self):#增加一个单位
        self.driver.find_element_by_css_selector(".tabmenu_content > div:nth-child(1) > ul:nth-child(16) > li:nth-child(1)").click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame("tab_SysOrganization_ifm")
        self.driver.find_element_by_class_name("border").send_keys("特勤部")
        self.driver.find_element_by_id("FormView1_OrderNoTextBox").clear()
        self.driver.find_element_by_id("FormView1_OrderNoTextBox").send_keys(1)
        self.driver.find_element_by_id("FormView1_ibtManage").click()
        self.driver.switch_to.frame(1)
        self.driver.find_element_by_id("TreeView1n3CheckBox").click()
        self.driver.find_element_by_id("btn_Ok").click()
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame("tab_SysOrganization_ifm")
        self.driver.find_element_by_id("FormView1_ibtRead").click()
        self.driver.switch_to.frame(1)
        self.driver.find_element_by_id("TreeView1n6CheckBox").click()
        self.driver.find_element_by_id("btn_Ok").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("tab_SysOrganization_ifm")
        time.sleep(3)
        self.driver.find_element_by_id("FormView1_btnSave").click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
    def test_case2(self):#删除一个机构
        self.driver.find_element_by_css_selector(
            ".tabmenu_content > div:nth-child(1) > ul:nth-child(16) > li:nth-child(1)").click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame("tab_SysOrganization_ifm")
        self.driver.find_element_by_id("TreeView1t1").click()
        time.sleep(3)
        self.driver.find_element_by_id("FormView1_DeleteButton").click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
    def test_case3(self):#增加一个部门
        self.driver.find_element_by_css_selector(
            ".tabmenu_content > div:nth-child(1) > ul:nth-child(16) > li:nth-child(1)").click()#打开机构管理
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame("tab_SysOrganization_ifm")#进入框架
        self.driver.find_element_by_id("TreeView1t7").click()#进入“特勤部”
        time.sleep(3)
        self.driver.find_element_by_id("FormView1_NewButton").click()#点击新增
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("FormView1_NameTextBox11").send_keys("狼人杀俱乐部")#输入机构名称
        self.driver.find_element_by_id("FormView1_OrderNoTextBox11").clear()#清空显示顺序
        self.driver.find_element_by_id("FormView1_OrderNoTextBox11").send_keys("2")#输入显示顺序
        self.driver.find_element_by_id("FormView1_ibtManage").click()#点击主管领导菜单
        time.sleep(3)
        self.driver.switch_to.frame(1)#进入子框架
        self.driver.find_element_by_id("TreeView1n4CheckBox").click()#选择部门领导
        self.driver.find_element_by_id("btn_Ok").click()#点击确定
        time.sleep(3)
        self.driver.switch_to.default_content()#退出所有框架
        self.driver.switch_to.frame("tab_SysOrganization_ifm")#进入父级框架
        self.driver.find_element_by_id("FormView1_ibtRead").click()#点击机构共享菜单
        time.sleep(3)
        self.driver.switch_to.frame(1)#进入子框架
        self.driver.find_element_by_id("TreeView1n6CheckBox").click()#选择总经理
        self.driver.find_element_by_id("btn_Ok").click()#点击确定
        self.driver.switch_to.default_content()#退出框架
        time.sleep(3)
        self.driver.switch_to.frame("tab_SysOrganization_ifm")  # 进入父级框架
        self.driver.find_element_by_id("FormView1_btnSave").click()#点击保存
        self.driver.switch_to.alert.accept()
        time.sleep(3)
    def test_case4(self):#修改一个部门
        self.driver.find_element_by_css_selector(
            ".tabmenu_content > div:nth-child(1) > ul:nth-child(16) > li:nth-child(1)").click()#打开机构管理
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame("tab_SysOrganization_ifm")#进入框架
        self.driver.find_element_by_id("TreeView1t7").click()#进入“特勤部”
        time.sleep(3)
        self.driver.find_element_by_id("FormView1_NameTextBox12").clear()#清空机构名称
        self.driver.find_element_by_id("FormView1_NameTextBox12").send_keys("大神云集区")##修改机构名称
        # time.sleep(3)
        # self.driver.find_element_by_id("FormView1_fupIcon").send_keys("C:\\Users\\Administrator\\Desktop\\dlrb")
        # time.sleep(3)
        self.driver.find_element_by_id("FormView1_btnSave").click()#点击保存
        time.sleep(3)
        self.driver.switch_to.alert.accept()
    def tearDown(self):
        self.driver.switch_to.default_content()
        self.driver.quit()
if __name__=="__main__":
    unittest.main()








