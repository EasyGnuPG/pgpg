import sys
import textwrap
import time

import gpg

from fn.auxilary import handle_exception, print_debug


def print_signatures(verify_result):
    c = gpg.Context()
    for signature in verify_result.signatures:
        user = c.get_key(signature.fpr).uids[0].uid
        fpr = signature.fpr
        signed_time = time.ctime(signature.timestamp)

        message = '''
                  Good signature from "{user}"
                  with key {fingerprint}
                  made at {time}
                  '''.format(user=user,
                             fingerprint=fpr,
                             time=signed_time)

        print(textwrap.dedent(message))


@handle_exception(gpg.errors.GpgError, PermissionError, FileNotFoundError)
def open_file(sealed_file_path, output_file_path):
    c = gpg.Context()
    with open(sealed_file_path, "rb") as cfile:
        plaintext, result, verify_result = c.decrypt(
            cfile, verify=True)

        print_debug(verify_result, result)

        print_signatures(verify_result)

    with open(output_file_path, "wb") as nfile:
        nfile.write(plaintext)


if __name__ == "__main__":
    sealed_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    open_file(sealed_file_path, output_file_path)
