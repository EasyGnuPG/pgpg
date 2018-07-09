import sys
from fn.interact import interact


def trust(contact, level):
    commands = ";trust;;{level};;quit;;".format(level=level).split(";")
    try:
        interact(contact, commands)
    except BaseException:
        print("Error changing trust",
              file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    contact = sys.argv[1]
    level = sys.argv[2]
    trust(contact, level)
