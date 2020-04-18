from random import randrange
from models.contact import Contact
import re


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None,
                          [contact.home, contact.mobile, contact.work,
                           contact.phone2]))))


def merge_emails(contact):
    return "\n".join(
        filter(lambda x: x != "",
               filter(lambda x: x is not None,
                      [contact.email, contact.email2, contact.email3])))


def test_contact_from_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nkk", lastname="Lok", home="573",
                                   address="gdgrdv", work="231", mobile="3243",
                                   phone2="674239", email="fff@ff.ff",
                                   email2="njj@gg.ss"))

    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_homepage = contact_list[index]
    contact_from_edit = app.contact.get_contact_from_edit(index)

    assert contact_from_homepage.lastname == contact_from_edit.lastname
    assert contact_from_homepage.firstname == contact_from_edit.firstname
    assert contact_from_homepage.address == contact_from_edit.address
    assert contact_from_homepage.all_emails == merge_emails(contact_from_edit)
    assert contact_from_homepage.all_phones == merge_phones(contact_from_edit)
