import gpg
import sys
import os


def revoke(revcert_path):
    c = gpg.Context()
    try:
        with open(revcert_path) as revcert_file:
            c.op_import(revcert_file)
            result = c.op_import_result()
            if result is None:
                print("Error in revokation")
                exit(1)
    except (gpg.errors.GpgError, PermissionError, FileNotFoundError) as e:
        if os.environ['DEBUG'] == 'yes':
            raise
        print(e, file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    revcert_path = sys.argv[1]
    revoke(revcert_path)
