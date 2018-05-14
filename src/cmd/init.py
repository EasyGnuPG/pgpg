import gpg
import os
import sys
import shutil

def cmd_init_help():
    print("""
    init [<dir>]
        Initialize egpg. Optionally give the directory
        to be used. If not given, the default directory
        will be $HOME/.egpg/
    """)

def cmd_init(path=None):
    if path:
        if os.path.isdir(path):
            yesno = input("There is an old directory " + path + ". Do you want to erase it? [Y/N]: ")
            if yesno.lower() == "y":
                shutil.rmtree(path)
            else:
                exit(1)
    else:
        basePath = os.environ.get("HOME")
        if basePath is None:
            print("Could not find environment variable $HOME. Please try again")
            exit(1)

        path = basePath + "/.egpg"
        if os.path.exists(path):
            yesno = input("There is an old directory " + path + ". Do you want to erase it? [Y/N]: ")
            if yesno.lower() == "y":
                shutil.rmtree(path)
            else:
                exit(1)

    os.makedirs(path)
    innerPath = path + "/.gnupg"
    os.makedirs(innerPath)
    with open(innerPath + "/gpg-agent.conf", "w") as agentConf:
        toWrite = """
quiet
pinentry-program /usr/bin/pinentry-tty
allow-loopback-pinentry
default-cache-ttl 300
max-cache-ttl 999999
"""
        agentConf.write(toWrite)

    with open(innerPath + "/gpg.conf", "w") as gpgConf:
        toWrite = """
keyid-format long
default-cert-expire 1y
"""
        gpgConf.write(toWrite)

    with open(path + "/config.sh", "w") as configFile:
        toWrite = """
# If true, push local changes to the keyserver network.
# Leave it empty (or comment it out) to disable.
SHARE=
#KEYSERVER=hkp://keys.gnupg.net

# GPG homedir. If "default", then the default one will be used,
# (whatever is in the environment $GNUPGHOME, usually ~/.gnupg).
GNUPGHOME="$(realpath "$EGPG_DIR")/.gnupg"

# Path of the dongle.
DONGLE=

# If true, print debug output.
DEBUG=
"""
        configFile.write(toWrite)

    env_setup(path, (os.environ.get("HOME") + "/.bashrc"))

def env_setup(path, rcFile):
    with open(rcFile, "a") as rc:
        toWrite = """
### start pgpg config
export GPG_TTY=$(tty)
export EGPG_DIR={}
#export GNUPGHOME={}/.gnupg
### end pgpg config
""".format(path, path)

        rc.write(toWrite)
        print("Appended the following lines to your .bashrc:")
        print(toWrite)
        print("Please reload it to enable the new config:\n\tsource ~/.bashrc")

def main():
    if len(sys.argv) == 0:
        cmd_init_help()
    if len(sys.argv) > 2:
        cmd_init(sys.argv[2])
    else:
        cmd_init()

if __name__ == "__main__":
    main()


