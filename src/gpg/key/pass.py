import gpg
import sys
import os


def passwd(keyid):
    try:
        c = gpg.Context()
        keys = list(c.keylist(keyid))
        key = keys[0]
        c.op_passwd(key, 0)

    except gpg.errors.GpgError as e:
        if os.environ["DEBUG"] == "yes":
            raise
        print(e, file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    keyid = sys.argv[1]
    passwd(keyid)
