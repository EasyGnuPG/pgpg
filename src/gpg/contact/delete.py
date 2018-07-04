import gpg
import sys
import os
from fn.print_key import print_key


def delete(contacts, force):
    try:
        c = gpg.Context()
        for contact in contacts:
            keys = list(c.keylist(contact))
            ans = "n"
            for key in keys:
                if(not force):
                    print_key(key.fpr, end="\n")
                    try:
                        ans = input("Delete this key from the keyring? (y/N)")
                    except EOFError:
                        exit(0)

                if(ans.lower() == 'y' or force):
                    c.op_delete(key, False)

    except BaseException:
        if(os.environ['DEBUG'] == 'yes'):
            raise
        exit(2)


if __name__ == "__main__":
    force = int(sys.argv[1])
    contacts = sys.argv[2:]
    delete(contacts, force)
