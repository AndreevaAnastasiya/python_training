from models.group import Group


def test_edit_name_first_group(app):
    app.group.edit_first(Group(name="new"))


def test_edit_header_first_group(app):
    app.group.edit_first(Group(header="new header"))
