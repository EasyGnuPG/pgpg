# Print the details of the given key id.
import os
import sys
import textwrap
import time

import gpg


def print_key(identity):
    """
    print the details of key whose identitiy is passed
    """
    c = gpg.Context()
    key = list(c.keylist(identity, mode=gpg.constants.keylist.mode.SIGS))

    # exit with status 1 if more than one key matches are found for identity
    if len(key) > 1:
        exit(1)
    else:
        key = key[0]

    if os.environ["DEBUG"] == "yes":
        print(key)
        print()

    # uid
    uid_list = ["uid: " + user_id.uid for user_id in key.uids]
    all_uids = "\n".join(uid_list)

    # fpr
    fpr = " ".join(textwrap.wrap(key.fpr, 4))

    # trust
    trust_map = {
        "UNKNOWN": "UNKNOWN",
        "UNDEFINED": "UNKNOWN",
        "ULTIMATE": "ULTIMATE",
        "NEVER": "NONE",
        "MARGINAL": "MARGINAL",
        "FULL": "FULL"
        }
    trust = filter(lambda t: eval("gpg.constants.validity." + t) ==
                   key.owner_trust, trust_map.keys())
    trust = trust_map[list(trust)[0]].lower()
    trust = "trust: " + trust if trust != "unknown" else ""

    # keys
    subkey_list = []
    for subkey in key.subkeys:
        subkey_id = subkey.keyid
        tformat = "%Y-%m-%d"
        start = time.strftime(tformat, time.localtime(subkey.timestamp))

        # check if key never expires
        endtime = time.localtime(subkey.expires)
        end = time.strftime(tformat, endtime) if endtime != 0 else "never"

        exp = "expired" if subkey.expired == 1 else ""

        if subkey.can_sign == 1:
            u = "sign"
        elif subkey.can_authenticate == 1:
            u = "auth"
        elif subkey.can_encrypt == 1:
            u = "decr"

        subkey_map = {
            "u": u,
            "subkey_id": subkey_id,
            "start": start,
            "end": end,
            "exp": exp
        }

        subkey_list.append("{u}: {subkey_id} {start} {end} {exp}"
                           .format_map(subkey_map))

    subkeys = "\n".join(subkey_list)

    # verifications
    sign_list = []
    for uid in key.uids:
        for sign in uid.signatures:
            if (sign.keyid != identity and
                    sign.revoked == 0 and sign.expired == 0):
                sign_list.append("certified by: " +
                                 sign.uid + " " + sign.keyid)

    signatures = "\n".join(sign_list)

    key_map = {
        "identity": identity,
        "all_uids": all_uids,
        "fpr": fpr,
        "trust": trust,
        "subkeys": subkeys,
        "signatures": signatures
    }

    print("id: {identity}\n"
          "{all_uids}\n"
          "fpr: {fpr}\n"
          "{trust}\n"
          "{subkeys}"
          "{signatures}"
          .format_map(key_map))


if __name__ == "__main__":
    try:
        identity = sys.argv[1]
        print_key(identity)
    except BaseException:
        if(os.environ["DEBUG"] == "yes"):
            raise
        exit(2)
