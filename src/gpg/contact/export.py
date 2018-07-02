import gpg
import sys
import os


def export(export_path, contacts):
    c = gpg.Context(armor=True)

    if(export_path == "-"):
        export_file = sys.stdout
    else:
        export_file = open(export_path, "w")

    try:
        for user in contacts:
            expkey = gpg.Data()
            c.op_export(user, 0, expkey)
            expkey.seek(0, os.SEEK_SET)
            expstring = expkey.read()
            if expstring:
                export_file.write(expstring.decode())
            else:
                sys.stderr.write("No keys found for %s \n" % user)
                exit(1)

    except BaseException:
        if os.environ['DEBUG'] == 'yes':
            raise
        exit(2)

    if(export_path != "-"):
        export_file.close()


if __name__ == "__main__":
    export_path = sys.argv[1]
    contacts = [None]
    if (len(sys.argv) > 2):
        contacts = sys.argv[2:]
    print(contacts)
    export(export_path, contacts)
