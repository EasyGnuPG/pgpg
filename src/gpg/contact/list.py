import gpg
import sys
import os
from fn.print_key import print_key


def ls(contact_list):
    """
    list the contacts in contact list
    """
    try:
        c = gpg.Context()

        key_set = set({})

        for contact in contact_list:
            key_set.update(set(c.keylist(contact)))

        if len(list(key_set)) == 0:
            print("No matching contacts found!")
            exit(0)

        for key in key_set:
            print_key(key.fpr, end="\n")
    
    except BaseException:
        exit(1)


if __name__ == "__main__":
    contacts = [None]
    if (len(sys.argv) > 1):
        contacts = sys.argv[1:]

    if os.environ['DEBUG'] == 'yes':
        print("contacts:", contacts, sep="\n")

    ls(contacts)
