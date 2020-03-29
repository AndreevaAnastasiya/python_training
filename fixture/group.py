
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("group page").click()

    def fill_form(self, group):
        dw = self.app.dw
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").send_keys(group.footer)

    def clear_fields(self):
        dw = self.app.dw
        dw.find_element_by_name("group_name").clear()
        dw.find_element_by_name("group_header").clear()
        dw.find_element_by_name("group_footer").clear()

    def create(self, group):
        dw = self.app.dw
        self.open_group_page()
        dw.find_element_by_name("new").click()
        self.fill_form(group)
        dw.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first(self):
        dw = self.app.dw
        self.open_group_page()
        dw.find_element_by_name("selected[]").click()
        dw.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        dw = self.app.dw
        self.open_group_page()
        dw.find_element_by_name("selected[]").click()
        dw.find_element_by_name("edit").click()
        self.clear_fields()
        self.fill_form(group)
        dw.find_element_by_name("update").click()
        self.return_to_groups_page()
