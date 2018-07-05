import gpg
import sys
import os
from fn.print_key import print_key


def list_contacts(contacts):
    try:
        c = gpg.Context()

        key_set = set()

        for contact in contacts:
            key_set.update(c.keylist(contact))

        if len(list(key_set)) == 0:
            print("No matching contacts found!")
            exit(0)

        for key in key_set:
            print_key(key.fpr, end="\n")
    
    except BaseException:
        if os.environ["DEBUG"] == 'yes':
            raise
        exit(1)


if __name__ == "__main__":
    contacts = [None]
    if len(sys.argv) > 1:
        contacts = sys.argv[1:]

    if os.environ['DEBUG'] == 'yes':
        print("contacts:", contacts, sep="\n")

    list_contacts(contacts)
