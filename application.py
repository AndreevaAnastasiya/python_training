from selenium import webdriver
from selenium.webdriver.support.select import Select


class Application:

    def __init__(self):
        self.dw = webdriver.Chrome()
        self.dw.implicitly_wait(30)

    def login(self, username, password):
        dw = self.dw
        dw.get("http://localhost:8080/addressbook/index.php")
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def create_group(self, group):
        dw = self.dw
        dw.find_element_by_link_text("groups").click()
        dw.find_element_by_name("new").click()
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").send_keys(group.footer)
        dw.find_element_by_name("submit").click()
        dw.find_element_by_link_text("groups").click()

    def create_contact(self, contact):
        dw = self.dw
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
        dw.find_element_by_link_text("home").click()

    def logout(self):
        dw = self.dw
        dw.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.dw.quit()
