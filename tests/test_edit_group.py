from models.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="safcd", header="dsfvfde", footer="fvfds"))
    app.session.logout()
