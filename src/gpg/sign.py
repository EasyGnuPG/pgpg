import sys

import gpg

from fn.auxilary import handle_exception


@handle_exception(gpg.errors.GpgError, PermissionError, FileNotFoundError)
def sign(key, filename):
    sig_src = list(gpg.Context().keylist(pattern=key, secret=True))
    c = gpg.Context(signers=sig_src, armor=True)
    with open(filename, "rb") as tfile:
        text = tfile.read()

    signed_data, _result = c.sign(text, mode=gpg.constants.sig.mode.DETACH)

    with open(filename+".signature", "wb") as afile:
        afile.write(signed_data)


if __name__ == "__main__":
    key, filename = sys.argv[1], sys.argv[2]
    sign(key, filename)
