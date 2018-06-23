import sys
import gpg
import time
import textwrap


def verify(signature_file, filename):
    """
    verify the signature
    signature_file has the detached signature
    filename has the name of the file which is signed
    """

    c = gpg.Context()

    try:
        _, result = c.verify(open(filename), open(signature_file))
        verified = True
    except gpg.errors.BadSignatures as e:
        verified = False
        print(e)

    if verified is True:
        for signature in result.signatures:
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


if __name__ == "__main__":
    signature_file, filename = sys.argv[1], sys.argv[2]
    verify(signature_file, filename)
