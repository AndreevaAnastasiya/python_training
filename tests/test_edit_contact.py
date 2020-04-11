from models.contact import Contact


def test_edit_firstname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nkk", nickname="Lok"))

    old_contacts = app.contact.get_contact_list()

    contact = Contact(firstname="Lia")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname

    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)


def test_edit_lastname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Bro", lastname="Lu"))

    old_contacts = app.contact.get_contact_list()

    contact = Contact(lastname="Nyt")
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname

    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
