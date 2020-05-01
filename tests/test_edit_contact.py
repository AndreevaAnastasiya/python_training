from models.contact import Contact
import random


def test_edit_firstname_contact_by_index(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Nkk", nickname="Lok"))

    old_contacts = db.get_contact_list()

    contact_by_edit = random.choice(old_contacts)
    contact = Contact(firstname="Lia")
    contact.id = contact_by_edit.id
    contact.lastname = contact_by_edit.lastname

    app.contact.edit_by_id(contact_by_edit.id, contact)
    new_contacts = db.get_contact_list()

    for element in old_contacts:
        if element == contact_by_edit:
            element.firstname = contact.firstname

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.id_or_max)


def test_edit_lastname_contact_by_index(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Bro", lastname="Lu"))

    old_contacts = db.get_contact_list()

    contact_by_edit = random.choice(old_contacts)
    contact = Contact(lastname="Nyt")
    contact.id = contact_by_edit.id
    contact.firstname = contact_by_edit.firstname

    app.contact.edit_by_id(contact_by_edit.id, contact)
    new_contacts = db.get_contact_list()

    for element in old_contacts:
        if element == contact_by_edit:
            element.lastname = contact.lastname

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.id_or_max)
