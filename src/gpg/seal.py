import gpg
import os
import sys


def in_keyring(recipient):
    """
    Check if a valid key is present in the keyring matching
    recipient
    """

    matched_keys = list(gpg.Context().keylist(recipient))
    valid_keys = list(filter(lambda k: k.revoked == 0 and k.expired == 0,
                             matched_keys))
    if len(valid_keys) == 0:
        return False
    else:
        return True


def get_selected_key(keys):
    """
    In case of multiple matches list the keys and confirm from the user.
    Currently displaying all at once; no N)ext functionality
    """

    all_keys = list(keys)
    valid_keys = list(filter(
        lambda k: k.revoked == 0 and k.expired == 0, all_keys))

    if len(valid_keys) == 1:
        return valid_keys

    for sno, key in enumerate(valid_keys):
        print(sno+1, key.uids[0].uid, key.fpr)

    chosen_keys = []
    while(True):
        try:
            print("Enter the number(s) to select a key, Q)uit", end='>')
            indices = input().strip().split()
            for index in indices:
                if index.lower() == 'q':
                    return None
                else:
                    chosen_keys.append(valid_keys[int(index)-1])

            return chosen_keys

        except (IndexError, ValueError):
            print("Please enter a valid choice")


def seal(file_path, recipients):
    """
    sign and encrypt file_path to the recipents
    """

    try:
        c = gpg.Context(armor=True)
        c.signers = list(c.keylist(pattern=None, secret=True))
        seal_list = []

        # prepare the list
        for recipient in recipients:
            keys = c.keylist(pattern=recipient)
            chosen_keys = get_selected_key(list(keys))
            seal_list.extend(chosen_keys)

        # print the list
        print("The following recipients were selected:")
        for sno, key in enumerate(seal_list):
            print(str(sno+1) + ")", key.uids[0].uid, key.fpr)

        # encrypt
        seal_path = file_path+".sealed"
        with open(file_path) as infile:
            with open(seal_path, "w") as outfile:
                try:
                    _cyphertext, _result, _sign_result = c.encrypt(
                        infile, recipients=seal_list,
                        sign=True, sink=outfile)
                except gpg.errors.InvalidRecipients:
                    print("Some of the recipients are not trusted."
                          " Do you want to proceed anyway[y/N]", end='>')
                    answer = input().lower()
                    if answer == 'y' or answer == 'yes':
                        _cyphertext, _result, _sign_result = c.encrypt(
                            infile, recipients=seal_list, sign=True,
                            sink=outfile, always_trust=True)
                    else:
                        exit(3)

    except BaseException:
        if os.environ['DEBUG'] == 'yes':
            raise
        exit(2)


if __name__ == "__main__":
    file_path = sys.argv[1]
    recipients = sys.argv[2:]

    for recipient in recipients:
        if not in_keyring(recipient):
            sys.stderr.write("Sorry! No matching contact for `{recipient}`\n"
                             "Please add the person to your contacts first!\n"
                             "For help on adding contacts run"
                             "`egpg contact help`\n\n"
                             .format(recipient=recipient))
            exit(1)

    seal(file_path, recipients)
