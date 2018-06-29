import gpg
import sys
import os


def gen(parameters):
    params = """<GnupgKeyParms format="internal">
    {parameters}
    </GnupgKeyParms>
    """.format(parameters=parameters)

    c = gpg.Context()
    c.op_genkey(params, None, None)
    print("Generated key with fingerprint {fpr}.".format(
          fpr=c.op_genkey_result().fpr))


if __name__ == "__main__":
    parameters = sys.argv[1]
    try:
        gen(parameters)
    except BaseException:
        if os.environ["DEBUG"] == "yes":
            raise
        else:
            exit(1)
