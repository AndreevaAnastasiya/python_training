# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Ann", middlename="", lastname="Fox",
                               nickname="Anna", company="Azure", address="str",
                               home="1256", mobile="875733", work="43856",
                               fax="47562735", email="ann@mail.ru", email2="",
                               email3="", homepage="anna.com", bday='1',
                               bmonth='May', byear='1990'))
