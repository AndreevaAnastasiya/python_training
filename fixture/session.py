
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
