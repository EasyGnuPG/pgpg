import sys

import gpg

from fn.auxilary import handle_exception


@handle_exception(gpg.errors.GpgError)
def delete(key_id):
    c = gpg.Context()
    keys = list(c.keylist(key_id))
    for key in keys:
        c.op_delete(key, True)


if __name__ == "__main__":
    key_id = sys.argv[1]
    delete(key_id)
