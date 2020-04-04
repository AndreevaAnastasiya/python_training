from models.contact import Contact


def test_edit_nickname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="JHBJ", nickname="J"))
    app.contact.edit_first(Contact(nickname="Lia"))


def test_edit_address_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="JHBJ", address="djvg"))
    app.contact.edit_first(Contact(address="street 5"))
