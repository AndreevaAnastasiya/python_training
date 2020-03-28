from models.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="Lia", middlename="", lastname="J",
                               nickname="Lia", company="Azure", address="str",
                               homephone="45245", mobile="53733", work="43436",
                               fax="4262735", email="lia@mail.ru", email2="",
                               email3="", homepage="lia.com", bday='3',
                               bmonth='April', byear='1991'))
    app.session.logout()
