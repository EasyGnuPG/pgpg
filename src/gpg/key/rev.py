import sys

import gpg

from fn.auxilary import fail, handle_exception


@handle_exception(gpg.errors.GpgError, PermissionError, FileNotFoundError)
def revoke(revcert_path):
    c = gpg.Context()
    with open(revcert_path) as revcert_file:
        c.op_import(revcert_file)
        result = c.op_import_result()
        if result is None:
            fail("Error in revocation")


if __name__ == "__main__":
    revcert_path = sys.argv[1]
    revoke(revcert_path)
