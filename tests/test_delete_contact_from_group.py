from models.contact import Contact
from models.group import Group
from fixture.orm import ORMFixture
import random


def test_delete_contact_from_group(app):
    db = ORMFixture(host="localhost", name="addressbook", user="root",
                    password="")

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Bro", lastname="Lu"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group1", header="header1",
                         footer="footer1"))

    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contact_list()
    contact = random.choice(contacts)

    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(contact.id, group.id)

    contacts_in_group = db.get_contacts_in_group(group)
    contact_for_delete = random.choice(contacts_in_group)

    app.contact.delete_contact_from_group(contact_for_delete.id, group.id)

    contacts_not_in_group = db.get_contacts_not_in_group(group)
    assert contact_for_delete in contacts_not_in_group
