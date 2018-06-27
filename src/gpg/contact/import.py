import gpg
import sys
import os


def import_contact(import_path):
    c = gpg.Context()
    try:
        with open(import_path) as import_file:
            c.op_import(import_file)
            result = c.op_import_result()
            if result is None:
                exit(1)
    except BaseException:
        if os.environ['DEBUG'] == 'yes':
            raise
        exit(2)


if __name__ == "__main__":
    import_path = sys.argv[1]
    import_contact(import_path)
