from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None,
                 nickname=None, company=None, address=None, home=None,
                 mobile=None, work=None, fax=None, phone2=None, email=None,
                 email2=None, email3=None, homepage=None, bday=None,
                 bmonth=None, byear=None, id=None, all_phones=None,
                 all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.phone2 = phone2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.all_phones = all_phones
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,
                                self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
            and self.firstname == other.firstname\
            and self.lastname == other.lastname\
            and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
