import os
import sys
from fn.interact import interact


def trust(contact, level):
    commands = [None, "trust", None, level, None, "quit", None, None]
    try:
        interact(contact, commands)
    except BaseException:
        if os.environ["DEBUG"] == "yes":
            raise
        print("Error changing trust",
              file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    contact = sys.argv[1]
    level = sys.argv[2]
    trust(contact, level)
