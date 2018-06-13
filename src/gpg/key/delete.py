import gpg
import sys
import os

def delete(key_id):
    try:
        c = gpg.Context()
        keys = list(c.keylist(key_id))
        for key in keys:
            c.op_delete(key,True)
            
    except BaseException:
        if(os.environ['DEBUG']=='yes'):
            raise
        exit(2)

if __name__ == "__main__":
    key_id = sys.argv[1]
    delete(key_id)