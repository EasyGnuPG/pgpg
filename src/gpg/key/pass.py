import sys

import gpg

from fn.auxiliary import handle_exception


@handle_exception(gpg.errors.GpgError)
def passwd(keyid):
    c = gpg.Context()
    keys = list(c.keylist(keyid))
    key = keys[0]
    c.op_passwd(key, 0)


if __name__ == "__main__":
    keyid = sys.argv[1]
    passwd(keyid)
