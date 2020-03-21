# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from group import Group


class AddTestGroup(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Chrome()
        self.dw.implicitly_wait(30)

    def open_groups_page(self, dw):
        dw.get("http://localhost:8080/addressbook/group.php")

    def login(self, dw, username, password):
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def create_group(self, dw, group):
        # init group creation
        dw.find_element_by_name("new").click()
        # fill group form
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        dw.find_element_by_name("submit").click()

    def return_to_groups_page(self, dw):
        dw.find_element_by_link_text("groups").click()

    def logout(self, dw):
        dw.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        dw = self.dw
        self.open_groups_page(dw)
        self.login(dw, username="admin", password="secret")
        self.create_group(dw, Group(name="dddd", header="dddd", footer="dddd"))
        self.return_to_groups_page(dw)
        self.logout(dw)

    def test_add_empty_group(self):
        dw = self.dw
        self.open_groups_page(dw)
        self.login(dw, username="admin", password="secret")
        self.create_group(dw, Group(name="", header="", footer=""))
        self.return_to_groups_page(dw)
        self.logout(dw)

    def tearDown(self):
        self.dw.quit()


if __name__ == "__main__":
    unittest.main()
