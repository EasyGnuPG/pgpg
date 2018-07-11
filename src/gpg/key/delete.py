import gpg
import sys
import os


def delete(key_id):
    try:
        c = gpg.Context()
        keys = list(c.keylist(key_id))
        for key in keys:
            c.op_delete(key, True)

    except gpg.errors.GpgError as e:
        if os.environ["DEBUG"] == "yes":
            raise
        print(e, file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    key_id = sys.argv[1]
    delete(key_id)
