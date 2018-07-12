import sys

import gpg

from fn.auxiliary import handle_exception
from fn.interact import interact


@handle_exception(gpg.errors.GpgError)
def trust(contact, level):
    commands = [None, "trust", None, level, None, "quit", None, None]
    interact(contact, commands)


if __name__ == "__main__":
    contact = sys.argv[1]
    level = sys.argv[2]
    trust(contact, level)
