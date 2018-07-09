import sys
from fn.interact import interact


def renew(key, time):
    commands = ";expire;;{time};;key 1;;expire;;{time};;save;;".format(
        time=time).split(";")
    try:
        interact(key, commands)
    except BaseException:
        print("Error renewing {key}".format(key=key),
              file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    key = sys.argv[1]
    time = sys.argv[2]
    renew(key, time)
