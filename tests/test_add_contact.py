# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ann", middlename="", lastname="Fox",
                      nickname="Anna", company="Azure", address="str",
                      home="1256", mobile="875733", work="43856", fax="475625",
                      phone2="8740", email="ann@mail.ru", email2="", email3="",
                      homepage="ann.com", bday='1', bmonth='May', byear='1990')
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
