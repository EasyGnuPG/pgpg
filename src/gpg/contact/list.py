import sys

import gpg

from fn.auxilary import fail, handle_exception, print_debug
from fn.print_key import print_key


@handle_exception(gpg.errors.GpgError)
def list_contacts(contacts):
    c = gpg.Context()

    key_set = set()

    for contact in contacts:
        key_set.update(c.keylist(contact))

    if len(list(key_set)) == 0:
        fail("No matching contacts found!")

    for key in key_set:
        print_key(key.fpr, end="\n")


if __name__ == "__main__":
    contacts = [None]
    if len(sys.argv) > 1:
        contacts = sys.argv[1:]

    print_debug("contacts:", contacts, sep="\n")

    list_contacts(contacts)
