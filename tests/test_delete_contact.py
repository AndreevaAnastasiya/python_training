from models.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="JHBJ", nickname="J"))
    app.contact.delete_first()
