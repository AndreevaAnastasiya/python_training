
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        dw = self.app.dw
        dw.get("http://localhost:8080/addressbook/index.php")
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        dw = self.app.dw
        dw.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        dw = self.app.dw
        return len(dw.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        dw = self.app.dw
        return dw.find_element_by_xpath(
            "//div/div[1]/form/b").text == "("+username+")"

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
