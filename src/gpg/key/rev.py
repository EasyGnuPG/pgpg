import gpg
import sys
import os

def revoke(revcert_path):
    c = gpg.Context()
    try:
        with open(revcert_path) as revcert_file:
            c.op_import(revcert_file)
            result = c.op_import_result()
            if result is None:
                exit(1)
    except BaseException:
        if(os.environ['DEBUG']=='yes'):
            raise
        exit(2)

if __name__ == "__main__":
    revcert_path=sys.argv[1]
    revoke(revcert_path)