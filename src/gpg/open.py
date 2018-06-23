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
                    Good signature from {user}
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
                print("Could not verify signatures")
                exit(3)

        while(os.path.exists(output_file_path)):
            print("File {output} already exists"
                  .format(output=output_file_path))
            print("Do you want to overwrite?(y/N)", end=">")

            ans = input()
            if ans.lower() == 'y':
                break
            else:
                print("New file name", end=":")
                output_file_path = input()

        with open(output_file_path, "wb") as nfile:
            nfile.write(plaintext)

    except BaseException:
        if os.environ['DEBUG'] == 'yes':
            raise
        else:
            exit(2)


if __name__ == "__main__":
    sealed_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    open_file(sealed_file_path, output_file_path)
