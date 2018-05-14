import gpg


key = "0x12345678DEADBEEF"
text = b"""Testing code.

Hello, world. This is a test of the GPGME bindings for Python3
"""

c = gpg.Context(armor=True)
rkey = list(c.keylist(pattern=key, secret=False))
ciphertext, result, signed_result = c.encrypt(text, recipients=rkey, sign=False)

print(ciphertext)
