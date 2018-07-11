import os
import sys
import gpg
from fn.interact import interact


def renew(key, time):
    commands = [None, "expire", None, time, None,
                "key 1", None, "expire", None, time, None,
                "save", None, None]
    try:
        interact(key, commands)
    except gpg.errors.GpgError as e:
        if os.environ["DEBUG"] == "yes":
            raise
        print(e, file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    key = sys.argv[1]
    time = sys.argv[2]
    renew(key, time)
