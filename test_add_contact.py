# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Ann", middlename="", lastname="Fox",
                               nickname="Anna", company="Azure", address="str",
                               homephone="1256", mobile="875733", work="43856",
                               fax="47562735", email="ann@mail.ru", email2="",
                               email3="", homepage="anna.com", bday='1',
                               bmonth='May', byear='1990'))
    app.logout()
