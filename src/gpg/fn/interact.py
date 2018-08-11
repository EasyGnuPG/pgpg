import gpg

from fn.auxiliary import debug, fail, handle_exception, print_debug


class KeyEditor(object):
    def __init__(self, cmds, verbose=False):
        self.cmds = cmds
        self.step = 0
        self.done = False

    def edit_fnc(self, status, args, out=None):
        print_debug("Code: {status}, args: {args}\n"
                    .format(status=status, args=args))

        # There may be multiple attempts to pinentry
        if status == "PINENTRY_LAUNCHED":
            cmd = None
        else:
            cmd = self.cmds[self.step]
            self.step += 1
            self.done = True if len(self.cmds) == self.step else False

        if debug:
            print_debug("cmd: {cmd}\n".format(cmd=cmd))
            try:
                input("Debug mode: Press any key to continue!")
            except EOFError:
                pass

        return cmd


@handle_exception(gpg.errors.GpgError, AssertionError)
def interact(key, commands):
    c = gpg.Context()
    keys = list(c.keylist(key))
    print_debug(keys, end="\n\n")

    if len(keys) != 1:
        if len(keys) == 0:
            error_msg = r"No key matching {key}"
        else:
            error_msg = r"More than 1 matching keys for {key}"
        fail(error_msg.format(key=key))

    editor = KeyEditor(commands, 2)
    c.interact(keys[0], editor.edit_fnc)
    assert editor.done
