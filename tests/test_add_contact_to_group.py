from models.contact import Contact
from models.group import Group
from fixture.orm import ORMFixture
import random


def test_add_contact_to_group(app):
    db = ORMFixture(host="localhost", name="addressbook", user="root",
                    password="")

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Bro", lastname="Lu"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group1", header="header1",
                         footer="footer1"))

    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)

    app.contact.add_contact_to_group(contact.id, group.id)

    contacts_in_group = db.get_contacts_in_group(group)
    assert contact in contacts_in_group
