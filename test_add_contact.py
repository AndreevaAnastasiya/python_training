# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

from selenium.webdriver.support.select import Select
from contact import Contact


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Chrome()
        self.dw.implicitly_wait(30)

    def open_home_page(self, dw):
        dw.get("http://localhost:8080/addressbook/index.php")

    def login(self, dw, username, password):
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, dw, contact):
        dw.find_element_by_link_text("add new").click()
        dw.find_element_by_name("firstname").send_keys(contact.firstname)
        dw.find_element_by_name("middlename").send_keys(contact.middlename)
        dw.find_element_by_name("lastname").send_keys(contact.lastname)
        dw.find_element_by_name("nickname").send_keys(contact.nickname)
        dw.find_element_by_name("company").send_keys(contact.company)
        dw.find_element_by_name("address").send_keys(contact.address)
        dw.find_element_by_name("home").send_keys(contact.homephone)
        dw.find_element_by_name("mobile").send_keys(contact.mobile)
        dw.find_element_by_name("work").send_keys(contact.work)
        dw.find_element_by_name("fax").send_keys(contact.fax)
        dw.find_element_by_name("email").send_keys(contact.email)
        dw.find_element_by_name("email2").send_keys(contact.email2)
        dw.find_element_by_name("email3").send_keys(contact.email3)
        dw.find_element_by_name("homepage").send_keys(contact.homepage)
        dw.find_element_by_name("bday").click()
        Select(dw.find_element_by_name("bday")).select_by_visible_text(
            contact.bday)
        dw.find_element_by_name("bmonth").click()
        Select(dw.find_element_by_name("bmonth")).select_by_visible_text(
            contact.bmonth)
        dw.find_element_by_name("byear").send_keys(contact.byear)
        dw.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_home_page(self, dw):
        dw.find_element_by_link_text("home").click()

    def logout(self, dw):
        dw.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        dw = self.dw
        self.open_home_page(dw)
        self.login(dw, username="admin", password="secret")
        self.create_contact(dw, Contact(firstname="Ann", middlename="",
                                        lastname="Fox", nickname="Anna",
                                        company="Azure", address="street 1",
                                        homephone="123456", mobile="877745733",
                                        work="36743856", fax="47562735",
                                        email="ann@mail.ru", email2="",
                                        email3="", homepage="anna.com",
                                        bday='1', bmonth='May', byear='1990'
                                        ))
        self.return_to_home_page(dw)
        self.logout(dw)

    def tearDown(self):
        self.dw.quit()


if __name__ == "__main__":
    unittest.main()
