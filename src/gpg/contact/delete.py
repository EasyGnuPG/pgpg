import sys

import gpg

from fn.auxilary import handle_exception
from fn.print_key import print_key


@handle_exception(gpg.errors.GpgError)
def delete(contacts, force):
    c = gpg.Context()
    for contact in contacts:
        keys = list(c.keylist(contact))
        ans = "n"
        for key in keys:
            if not force:
                print_key(key.fpr, end="\n")
                try:
                    ans = input("Delete this contact? (y/N)")
                except EOFError:
                    exit(0)

            if ans.lower() == 'y' or force:
                c.op_delete(key, False)


if __name__ == "__main__":
    force = int(sys.argv[1])
    contacts = sys.argv[2:]
    delete(contacts, force)
