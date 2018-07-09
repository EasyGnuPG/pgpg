import os
import sys
import gpg


class KeyEditor(object):
    def __init__(self, cmds, verbose=False):
        self.cmds = cmds
        self.step = 0
        self.done = False

    def edit_fnc(self, status, args, out=None):
        if os.environ["DEBUG"] == "yes":
            sys.stderr.write("Code: {status}, args: {args}\n"
                             .format(status=status, args=args))

        # There may be multiple attempts to pinentry
        if status == "PINENTRY_LAUNCHED":
            return None

        cmd = self.cmds[self.step]
        
        self.step += 1
        self.done = len(self.cmds) == self.step

        if os.environ["DEBUG"] == "yes":
            sys.stderr.write("cmd: {cmd}\n".format(cmd=cmd))
            try:
                input("Debug mode: Press any key to continue!")
            except EOFError:
                pass

        return cmd


def interact(key, commands):
    try:
        c = gpg.Context()
        keys = list(c.keylist(key))
        if os.environ["DEBUG"] == "yes":
            print(keys, end="\n\n")

        if len(keys) == 0:
            sys.stderr.write("No matching key found")
            exit(1)

        if len(keys) > 1:
            sys.stderr.write("More than one matching keys")
            exit(1)

        editor = KeyEditor(commands, 2)
        c.interact(keys[0], editor.edit_fnc)
        assert editor.done

    except BaseException:
        if os.environ["DEBUG"] == "yes":
            raise
        exit(2)
