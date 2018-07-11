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
                print("Could not import contact", file=sys.stderr,
                      flush=True)
                exit(1)
    except (gpg.errors.GpgError, FileNotFoundError) as e:
        if os.environ['DEBUG'] == 'yes':
            raise
        print(e, file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    import_path_list = sys.argv[1:]

    for import_path in import_path_list:
        import_contact(import_path)
