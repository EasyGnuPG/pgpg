import sys
import gpg
import time


def verify(signature_file, filename):
    """
    verify the signature
    signature_file has the detached signature
    filename has the name of the file which is signed
    """
    
    c = gpg.Context()
    
    try:
        _, result = c.verify(open(filename), open(signature_file))
        verified = True
    except gpg.errors.BadSignatures as e:
        verified = False
        print(e)

    if verified is True:
        for i in range(len(result.signatures)):
            sign = result.signatures[i]
            print(  
                'Signature made {2}\n'
                '\tusing key {1}\n'
                'Good signature from "{0}"'
                .format(c.get_key(sign.fpr).uids[0].uid,
                sign.fpr, time.ctime(sign.timestamp))         
            )


if __name__ == "__main__":
    signature_file, filename = sys.argv[1], sys.argv[2]
    verify(signature_file, filename)