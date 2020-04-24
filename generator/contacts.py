from models.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts,  args = getopt.getopt(sys.argv[1:],
                                "n:f:", ["numbers of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
            email2=random_string(10), email3=random_string(10)) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", f)

with open(file, "w") as out:
    out.write(jsonpickle.encode(testdata, indent=2))
