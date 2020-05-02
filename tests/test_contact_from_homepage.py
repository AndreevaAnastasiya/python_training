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


def test_contacts_from_homepage(app, db):
    all_emails_from_db = []
    all_emails_from_homepage = []
    all_phones_from_db = []
    all_phones_from_homepage = []

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Nkk", lastname="Lok", home="573",
                                   address="gdgrdv", work="231", mobile="3243",
                                   phone2="674239", email="fff@ff.ff",
                                   email2="njj@gg.ss"))

    contacts_list_from_db = db.get_contact_list()
    contacts_list_from_homepage = app.contact.get_contact_list()

    for element in contacts_list_from_db:
        element.all_emails = merge_emails(element)
        element.all_phones = merge_phones(element)
        all_emails_from_db.append(element.all_emails)
        all_phones_from_db.append(element.all_phones)

    for element in contacts_list_from_homepage:
        all_emails_from_homepage.append(element.all_emails)
        all_phones_from_homepage.append(element.all_phones)

    assert sorted(contacts_list_from_db, key=Contact.id_or_max) == sorted(
            contacts_list_from_homepage, key=Contact.id_or_max)

    assert sorted(all_phones_from_homepage) == sorted(all_phones_from_db)
    assert sorted(all_emails_from_homepage) == sorted(all_emails_from_db)
