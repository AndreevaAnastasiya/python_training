from selenium.webdriver.support.select import Select
from models.contact import Contact


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

    def delete_first(self):
        dw = self.app.dw
        self.open_home_page()
        dw.find_element_by_name("selected[]").click()
        dw.find_element_by_xpath("//input[@value='Delete']").click()
        dw.switch_to.alert.accept()

    def edit_first(self, contact):
        dw = self.app.dw
        self.open_home_page()
        dw.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_form(contact)
        dw.find_element_by_name("update").click()
        self.return_to_home_page()

    def count(self):
        dw = self.app.dw
        self.open_home_page()
        return len(dw.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        dw = self.app.dw
        self.open_home_page()
        contacts = []
        for element in dw.find_elements_by_xpath(
                "//input[@name='selected[]']/parent::td/parent::tr"):
            lastname = element.find_element_by_xpath(".//td[2]").text
            firstname = element.find_element_by_xpath(".//td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute(
                "value")
            contacts.append(Contact(lastname=lastname, firstname=firstname,
                                    id=id))
        return contacts
