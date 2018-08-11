import os
import sys

import gpg

from fn.auxiliary import handle_exception, print_debug, print_error


@handle_exception(PermissionError, gpg.errors.GpgError)
def export(export_path, homedir, contacts):
    c = gpg.Context(armor=True, home_dir=homedir)

    if export_path == "-":
        export_file = sys.stdout
    else:
        export_file = open(export_path, "w")

    for user in contacts:
        expkey = gpg.Data()
        c.op_export(user, 0, expkey)
        expkey.seek(0, os.SEEK_SET)
        expstring = expkey.read()
        if expstring:
            export_file.write(expstring.decode())
        else:
            print_error("No keys found for %s \n" % user)

    if export_path != "-":
        export_file.close()


if __name__ == "__main__":
    homedir = sys.argv[1]
    export_path = sys.argv[2]

    contacts = [None]
    if len(sys.argv) > 3:
        contacts = sys.argv[3:]

    print_debug("contacts:", contacts, sep="\n")

    export(export_path, homedir, contacts)
