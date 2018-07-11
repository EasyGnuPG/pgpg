import gpg
import sys
import os


def gen(parameters):
    try:
        params = """<GnupgKeyParms format="internal">
        {parameters}
        </GnupgKeyParms>
        """.format(parameters=parameters)

        c = gpg.Context()
        c.op_genkey(params, None, None)
        print("Generated key with fingerprint {fpr}.".format(
            fpr=c.op_genkey_result().fpr))
    except gpg.errors.GpgError as e:
        if os.environ["DEBUG"] == "yes":
            raise
        print(e, file=sys.stderr, flush=True)
        exit(1)


if __name__ == "__main__":
    parameters = sys.argv[1]
    gen(parameters)
