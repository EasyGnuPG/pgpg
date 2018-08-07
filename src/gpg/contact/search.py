import sys
import gpg
from fn.auxiliary import handle_exception, fail, print_debug
from fn.hkp import Server


@handle_exception()
def search(serverurl, searchstring):
    server = Server(serverurl)
    print_debug(server.serverurl)

    keys = server.index(searchstring)

    if keys in [None, []]:
        fail("No keys found")
    else:
        keysToImport = server.getchoice(keys)

    c = gpg.Context()
    for key in keysToImport:
        c.op_import(key.fullKey.encode())
        result = c.op_import_result()
        if result is None:
            fail("Could not import contact")
        print_debug(result)


if __name__ == "__main__":
    serverurl = sys.argv[1]
    searchstring = sys.argv[2]
    search(serverurl, searchstring)
