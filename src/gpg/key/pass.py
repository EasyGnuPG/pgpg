import gpg
import sys
import os


def passwd(keyid):
    c = gpg.Context()
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
