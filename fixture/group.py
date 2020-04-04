
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("group page").click()

    def select_first(self):
        dw = self.app.dw
        dw.find_element_by_name("selected[]").click()

    def change_field(self, field_name, text):
        dw = self.app.dw
        if text is not None:
            dw.find_element_by_name(field_name).clear()
            dw.find_element_by_name(field_name).send_keys(text)

    def fill_form(self, group):
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

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
        self.select_first()
        dw.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        dw = self.app.dw
        self.open_group_page()
        self.select_first()
        dw.find_element_by_name("edit").click()
        self.fill_form(group)
        dw.find_element_by_name("update").click()
        self.return_to_groups_page()

    def count(self):
        dw = self.app.dw
        self.open_group_page()
        return len(dw.find_elements_by_name("selected[]"))
