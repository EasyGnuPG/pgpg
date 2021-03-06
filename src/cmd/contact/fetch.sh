# Get contacts from another gpg directory.

cmd_contact_fetch_help() {
    cat <<-_EOF
    fetch [<contact>...] [-d,--homedir <gnupghome>]
        Get contacts from another gpg directory (by default from $GNUPGHOME).

_EOF
}

cmd_contact_fetch() {
    local opts homedir
    opts="$(getopt -o d: -l homedir: -n "$PROGRAM" -- "$@")"
    local err=$?
    eval set -- "$opts"
    while true; do
        case $1 in
            -d|--homedir) homedir="$2"; shift 2 ;;
            --) shift; break ;;
        esac
    done
    [[ $err == 0 ]] || fail "Usage:\n$(cmd_contact_fetch_help)"

    # get the gnupg dir
    [[ -n "$homedir" ]] || homedir="$ENV_GNUPGHOME"
    [[ -n "$homedir" ]] || fail "No gnupg directory to import from."
    [[ -d "$homedir" ]] || fail "Cannot find gnupg directory: $homedir"
    echo "Importing contacts from: $homedir"

    # export to tmp file
    workdir_make
    local file="$WORKDIR/contacts.asc"
    call_gpg contact/export.py "$homedir" "$file" "$@"

    # import from the tmp file
    call_gpg contact/import.py "$file"
    workdir_clear
}

#
# This file is part of EasyGnuPG.  EasyGnuPG is a wrapper around GnuPG
# to simplify its operations.  Copyright (C) 2016 Dashamir Hoxha
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/
#
