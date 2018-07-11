import sys

import gpg

from fn.auxilary import fail, handle_exception


@handle_exception(gpg.errors.GpgError, FileNotFoundError)
def import_contact(import_path):
    c = gpg.Context()
    with open(import_path) as import_file:
        c.op_import(import_file)
        result = c.op_import_result()
        if result is None:
            fail("Could not import contact")


if __name__ == "__main__":
    import_path_list = sys.argv[1:]

    for import_path in import_path_list:
        import_contact(import_path)
