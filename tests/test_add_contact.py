# -*- coding: utf-8 -*-
from models.contact import Contact
import pytest
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join(
        [random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phones(maxlen):
    symbols = string.digits + "-" + "(" + ")"
    return "".join(
        [random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string(7), lastname=random_string(10),
            home=random_phones(10), work=random_phones(10),
            email=random_string(10), mobile=random_phones(10),
            phone2=random_phones(10), address=random_string(15),
            email2=random_string(10), email3=random_string(10)) for i in range(3)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
