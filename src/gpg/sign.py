import sys
import gpg
import os


def sign(key, filename):
    """
    sign using key with armor and detach sign
    write to filename.signature
    """
    try:
        sig_src = list(gpg.Context().keylist(pattern=key, secret=True))
        c = gpg.Context(signers=sig_src, armor=True)
        with open(filename, "rb") as tfile:
            text = tfile.read()

        signed_data, _result = c.sign(text, mode=gpg.constants.sig.mode.DETACH)

        with open(filename+".signature", "wb") as afile:
            afile.write(signed_data)
    except (gpg.errors.GPGMEError, PermissionError, FileNotFoundError) as e:
        if os.environ["DEBUG"] == "yes":
            raise
        print(e, file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    key, filename = sys.argv[1], sys.argv[2]
    sign(key, filename)
