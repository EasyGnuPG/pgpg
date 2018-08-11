import sys
import textwrap
import time

import gpg

from fn.auxiliary import handle_exception


@handle_exception(gpg.errors.GpgError, PermissionError, FileNotFoundError)
def verify(signature_file, filename):
    c = gpg.Context()
    _, result = c.verify(open(filename), open(signature_file))

    for signature in result.signatures:
        message = '''
                    Good signature from "{user}"
                    with key {fingerprint}
                    made at {time}
                    '''.format(user=c.get_key(signature.fpr).uids[0].uid,
                               fingerprint=signature.fpr,
                               time=time.ctime(signature.timestamp))

        print(textwrap.dedent(message))


if __name__ == "__main__":
    signature_file, filename = sys.argv[1], sys.argv[2]
    verify(signature_file, filename)
