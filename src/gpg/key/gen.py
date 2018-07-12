import sys

import gpg

from fn.auxiliary import handle_exception


@handle_exception(gpg.errors.GpgError)
def generate_key(parameters):
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
    generate_key(parameters)
