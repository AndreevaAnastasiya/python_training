from selenium.webdriver.support.select import Select
from models.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        dw = self.app.dw
        if not (dw.current_url.endswith("/index.php") and len(
                dw.find_elements_by_xpath("//img[@title='Edit']")) > 0):
            dw.find_element_by_xpath("//a[contains(text(), 'home')]").click()

    def return_to_home_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("home").click()

    def change_field(self, field_name, text):
        dw = self.app.dw
        if text is not None:
            dw.find_element_by_name(field_name).clear()
            dw.find_element_by_name(field_name).send_keys(text)

    def change_select(self, field_name, value):
        dw = self.app.dw
        if value is not None:
            dw.find_element_by_name(field_name).click()
            Select(dw.find_element_by_name(field_name)).select_by_visible_text(
                value)

    def fill_form(self, contact):
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home)
        self.change_field("mobile", contact.mobile)
        self.change_field("work", contact.work)
        self.change_field("phone2", contact.phone2)
        self.change_field("fax", contact.fax)
        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
        self.change_field("homepage", contact.homepage)
        self.change_select("bday", contact.bday)
        self.change_select("bmonth", contact.bmonth)
        self.change_field("byear", contact.byear)

    def create(self, contact):
        dw = self.app.dw
        self.open_home_page()
        dw.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        dw.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_by_index(self, index):
        dw = self.app.dw
        self.open_home_page()
        dw.find_elements_by_name("selected[]")[index].click()
        dw.find_element_by_xpath("//input[@value='Delete']").click()
        dw.switch_to.alert.accept()
        self.contact_cache = None

    def open_to_edit_by_index(self, index):
        dw = self.app.dw
        self.open_home_page()
        dw.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def edit_by_index(self, index, contact):
        dw = self.app.dw
        self.open_to_edit_by_index(index)
        self.fill_form(contact)
        dw.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_view_by_index(self, index):
        dw = self.app.dw
        self.open_home_page()
        dw.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def count(self):
        dw = self.app.dw
        self.open_home_page()
        return len(dw.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            dw = self.app.dw
            self.open_home_page()
            self.contact_cache = []
            for element in dw.find_elements_by_xpath(
                    "//input[@name='selected[]']/parent::td/parent::tr"):
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute(
                    "value")
                all_phones = element.find_element_by_xpath(
                    ".//td[6]").text
                self.contact_cache.append(Contact(lastname=lastname, id=id,
                                                  firstname=firstname,
                                                  all_phones=all_phones))
        return list(self.contact_cache)

    def get_contact_from_edit(self, index):
        dw = self.app.dw
        self.open_to_edit_by_index(index)
        id = dw.find_element_by_name("id").get_attribute("value")
        firstname = dw.find_element_by_name("firstname").get_attribute("value")
        lastname = dw.find_element_by_name("lastname").get_attribute("value")
        home = dw.find_element_by_name("home").get_attribute("value")
        work = dw.find_element_by_name("work").get_attribute("value")
        mobile = dw.find_element_by_name("mobile").get_attribute("value")
        phone2 = dw.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home,
                       work=work, mobile=mobile, phone2=phone2)

    def get_contact_from_view(self, index):
        dw = self.app.dw
        self.open_view_by_index(index)
        text = dw.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)