from models.contact import Contact
from random import randrange


def test_delete_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="JHBJ", nickname="J"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) - 1 == len(new_contacts)

    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
