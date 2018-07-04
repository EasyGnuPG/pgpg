# Print the details of the given key id.
import os
import sys
import textwrap
import time

import gpg


def print_key(identity, end=""):
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
        print(key, end='\n\n')

    # uid
    uid_list = ["uid: " + user_id.uid + "\n" for user_id in key.uids]
    all_uids = "".join(uid_list)

    # fpr
    fpr = " ".join(textwrap.wrap(key.fpr, 4))

    # keyid
    keyid = key.fpr[-16:]

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
    trust = "trust: " + trust + "\n" if trust != "unknown" else ""

    # keys
    subkey_list = []
    for subkey in key.subkeys:
        starttime = time.strftime("%Y-%m-%d", time.localtime(subkey.timestamp))
        endtime = time.strftime("%Y-%m-%d", time.localtime(subkey.expires))

        # check if key never expires
        if subkey.expires == 0:
            endtime = "never"

        exp = "expired" if subkey.expired else ""

        if subkey.can_sign:
            u = "sign"
        elif subkey.can_authenticate:
            u = "auth"
        elif subkey.can_encrypt:
            u = "decr"

        subkey_map = {
            "u": u,
            "subkey_id": subkey.keyid,
            "start": starttime,
            "end": endtime,
            "exp": exp
        }

        subkey_list.append("{u}: {subkey_id} {start} {end} {exp}"
                           .format_map(subkey_map))

    subkeys = "\n".join(subkey_list) + "\n" if subkey_list else ""

    # verifications
    sign_list = set({})
    for uid in key.uids:
        for sign in uid.signatures:
            if (sign.keyid != keyid and sign.uid):
                if not (sign.revoked or sign.expired):
                    sign_list.add("certified by: " +
                                  sign.uid + " " + sign.keyid)

    signatures = "\n".join(sign_list) + "\n" if sign_list else ""

    key_map = {
        "identity": keyid,
        "all_uids": all_uids,
        "fpr": fpr,
        "trust": trust,
        "subkeys": subkeys,
        "signatures": signatures
    }

    print("id: {identity}\n"
          "{all_uids}"
          "fpr: {fpr}\n"
          "{trust}"
          "{subkeys}"
          "{signatures}"
          .format_map(key_map), end=end)


if __name__ == "__main__":
    try:
        identity = sys.argv[1]
        print_key(identity)
    except BaseException:
        if os.environ["DEBUG"] == "yes":
            raise
        exit(2)
