from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, contact):
        dw = self.app.dw
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

    def clear_fields(self):
        dw = self.app.dw
        dw.find_element_by_name("firstname").clear()
        dw.find_element_by_name("middlename").clear()
        dw.find_element_by_name("lastname").clear()
        dw.find_element_by_name("nickname").clear()
        dw.find_element_by_name("company").clear()
        dw.find_element_by_name("address").clear()
        dw.find_element_by_name("home").clear()
        dw.find_element_by_name("mobile").clear()
        dw.find_element_by_name("work").clear()
        dw.find_element_by_name("fax").clear()
        dw.find_element_by_name("email").clear()
        dw.find_element_by_name("email2").clear()
        dw.find_element_by_name("email3").clear()
        dw.find_element_by_name("homepage").clear()
        dw.find_element_by_name("byear").clear()

    def create(self, contact):
        dw = self.app.dw
        dw.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        dw.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        dw.find_element_by_link_text("home").click()

    def delete_first(self):
        dw = self.app.dw
        dw.find_element_by_name("selected[]").click()
        dw.find_element_by_xpath("//input[@value='Delete']").click()
        dw.switch_to.alert.accept()

    def edit_first(self, contact):
        dw = self.app.dw
        dw.find_element_by_xpath("//img[@title='Edit']").click()
        self.clear_fields()
        self.fill_form(contact)
        dw.find_element_by_name("update").click()
        dw.find_element_by_link_text("home").click()
