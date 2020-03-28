
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        dw = self.app.dw
        dw.find_element_by_link_text("groups").click()
        dw.find_element_by_name("new").click()
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").send_keys(group.footer)
        dw.find_element_by_name("submit").click()
        dw.find_element_by_link_text("groups").click()
