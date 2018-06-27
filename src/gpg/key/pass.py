import gpg
import sys
import os

try:
    autopin = os.environ["autopin"]
    sys.path.insert(0, autopin.rsplit("/", 1)[0])
    exec('import autopin')
    sys.path.pop(0)
except KeyError:
    autopin = None


def passwd(keyid):
    c = gpg.Context()
    if autopin is not None:
        c = autopin.setup(c)
    keys = list(c.keylist(keyid))

    if len(keys) != 1:
        if(os.environ["DEBUG"] == "yes"):
            print("`{num}` keys found. Shoud be only one key."
                  .format(num=len(keys)))
        exit(2)

    key = keys[0]
    c.op_passwd(key, 0)


if __name__ == "__main__":
    keyid = sys.argv[1]
    try:
        passwd(keyid)
    except BaseException:
        if os.environ["DEBUG"] == "yes":
            raise
        else:
            exit(1)
