import sys
import gpg
from fn.auxiliary import handle_exception, fail, print_debug
from fn.hkp import Server
import re


@handle_exception()
def receive(serverurl, keystring):
    pattern8 = re.compile(r"(^[0-9a-fA-F]{8}$)|(^[0-9a-fA-F]{16}$)")
    if re.match(pattern8, keystring) is None:
        fail("Invalid key pattern!")

    server = Server(serverurl)
    fullKey = server.get(keystring)

    if fullKey in [None, []]:
        fail("No keys found")

    c = gpg.Context()
    c.op_import(fullKey.encode())
    result = c.op_import_result()
    if result is None:
        fail("Could not import contact")
        print_debug(result)


if __name__ == "__main__":
    serverurl = sys.argv[1]
    keystring = sys.argv[2]
    receive(serverurl, keystring)
