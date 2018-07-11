import sys

import gpg

from fn.auxilary import handle_exception
from fn.interact import interact


@handle_exception(gpg.errors.GpgError)
def renew(key, time):
    commands = [None, "expire", None, time, None,
                "key 1", None, "expire", None, time, None,
                "save", None, None]
    interact(key, commands)


if __name__ == "__main__":
    key = sys.argv[1]
    time = sys.argv[2]
    renew(key, time)
