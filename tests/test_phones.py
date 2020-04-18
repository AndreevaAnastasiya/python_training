from random import randrange
from models.contact import Contact
import re


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nkk", lastname="Lok", home="573",
                                   address="gdgrdv", work="231", mobile="3243",
                                   phone2="674239"))

    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit = app.contact.get_contact_from_edit(index)

    assert contact_from_homepage.all_phones == merge_phones(contact_from_edit)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nkk", lastname="Lok", home="573",
                                   address="gdgrdv", work="231", mobile="3243",
                                   phone2="674239"))

    index = randrange(len(app.contact.get_contact_list()))
    contact_from_view = app.contact.get_contact_from_view(index)
    contact_from_edit = app.contact.get_contact_from_edit(index)

    assert contact_from_view.home == contact_from_edit.home
    assert contact_from_view.work == contact_from_edit.work
    assert contact_from_view.mobile == contact_from_edit.mobile
    assert contact_from_view.phone2 == contact_from_edit.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None,
                          [contact.home, contact.mobile, contact.work,
                           contact.phone2]))))
