from models.contact import Contact


def test_edit_nickname_first_contact(app):
    app.contact.edit_first(Contact(nickname="Lia"))


def test_edit_address_first_contact(app):
    app.contact.edit_first(Contact(address="street 5"))
