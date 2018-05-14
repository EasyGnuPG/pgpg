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
            if yesno.lower() is "y":
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                exit(1)
        else:
            os.makedirs(path)
    else:
        basePath = os.environ.get("HOME")
        if basePath is None:
            print("Could not find environment variable $HOME. Please try again")
            exit(1)
        fullPath = basePath + "/.egpg"
        if os.path.exists(fullPath):
            yesno = input("There is an old directory " + fullPath + ". Do you want to erase it? [Y/N]: ")
            if yesno.lower() is "y":
                shutil.rmtree(fullPath)
                os.makedirs(fullPath)
            else:
                exit(1)
        else:
            os.makedirs(fullPath)


def main():
    if len(sys.argv) == 0:
        cmd_init_help()
    print(str(sys.argv))
    if len(sys.argv) > 2:
        cmd_init(sys.argv[2])
    else:
        cmd_init()

if __name__ == "__main__":
    main()


