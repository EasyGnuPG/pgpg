import gpg


PIN = "123456"


def get_autopin(*args):
    global PIN
    return PIN


def setup(context):
    context.pinentry_mode = gpg.constants.PINENTRY_MODE_LOOPBACK
    context.set_passphrase_cb(get_autopin)
    return context
