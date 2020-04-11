from models.contact import Contact
from random import randrange


def test_edit_firstname_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nkk", nickname="Lok"))

    old_contacts = app.contact.get_contact_list()

    index = randrange(len(old_contacts))
    contact = Contact(firstname="Lia")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname

    app.contact.edit_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)


def test_edit_lastname_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Bro", lastname="Lu"))

    old_contacts = app.contact.get_contact_list()

    index = randrange(len(old_contacts))
    contact = Contact(lastname="Nyt")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname

    app.contact.edit_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
