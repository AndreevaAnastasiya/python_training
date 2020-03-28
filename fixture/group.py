
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("group page").click()

    def create(self, group):
        dw = self.app.dw
        self.open_group_page()
        dw.find_element_by_name("new").click()
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").send_keys(group.footer)
        dw.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first(self):
        dw = self.app.dw
        self.open_group_page()
        dw.find_element_by_name("selected[]").click()
        dw.find_element_by_name("delete").click()
        self.return_to_groups_page()
