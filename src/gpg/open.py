import gpg
import os
import sys
import time
import textwrap


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


def open_file(sealed_file_path, output_file_path):
    """
    sign and encrypt file_path to the recipents
    """

    try:
        c = gpg.Context()
        with open(sealed_file_path, "rb") as cfile:
            try:
                plaintext, result, verify_result = c.decrypt(
                    cfile, verify=True)

                if os.environ['DEBUG'] == 'yes':
                    print(verify_result, result)

                print_signatures(verify_result)

            except gpg.errors.BadSignatures:
                print("Could not verify signatures",
                      file=sys.stderr, flush=True)
                exit(1)

        with open(output_file_path, "wb") as nfile:
            nfile.write(plaintext)

    except (gpg.errors.GpgError, PermissionError, FileNotFoundError) as e:
        if os.environ['DEBUG'] == 'yes':
            raise
        print(e, file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    sealed_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    open_file(sealed_file_path, output_file_path)
