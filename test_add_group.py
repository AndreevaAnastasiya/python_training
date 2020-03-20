# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class AddTestGroup(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Chrome()
        self.dw.implicitly_wait(30)

    def test_add_group(self):
        dw = self.dw
        dw.get("http://localhost:8080/addressbook/group.php")
        dw.find_element_by_name("user").send_keys("admin")
        dw.find_element_by_name("pass").send_keys("secret")
        dw.find_element_by_xpath("//input[@value='Login']").click()
        dw.find_element_by_name("new").click()
        dw.find_element_by_name("group_name").send_keys("dddd")
        dw.find_element_by_name("group_header").send_keys("dddd")
        dw.find_element_by_name("group_footer").send_keys("dddd")
        dw.find_element_by_name("submit").click()
        dw.find_element_by_link_text("groups").click()
        dw.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try: self.dw.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.dw.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.dw.quit()


if __name__ == "__main__":
    unittest.main()
