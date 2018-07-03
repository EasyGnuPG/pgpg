import gpg
import sys
import os

def delete(contacts):
    try:
        c = gpg.Context()
        for contact in contacts:
            keys = list(c.keylist(contact))
            for key in keys:
                c.op_delete(key,False)
            
    except BaseException:
        if(os.environ['DEBUG']=='yes'):
            raise
        exit(2)

if __name__ == "__main__":
    contacts = sys.argv[1:]
    delete(contacts)