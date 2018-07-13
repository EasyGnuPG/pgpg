import requests


class Key:
    algomap = {
        "1": "RSA",
        "2": "RSA",
        "3": "RSA",
        "16": "Elgamal",
        "17": "DSA",
        "20": "Elgamal"
    }

    def __init__(self, pub, uids, fullkey=None):
        self.fpr = pub[0]

        try:
            self.algo = Key.algomap[pub[1]]
        except KeyError:
            self.algo = "Unknown"

        self.length = pub[2]
        self.start = pub[3]
        self.expire = pub[4]
        self.status = pub[5]

        self.uids = uids
        self.fullkey = fullkey

    def __str__(self):
        uidstring = "\n".join([x[0] for x in self.uids])
        rstring = uidstring + ("\n\t{length} bit {algo} key {fpr}, "
                               "created: {start} "
                               "expires: {end}".format(length=self.length,
                                                       algo=self.algo,
                                                       fpr=self.fpr[-16:],
                                                       start=self.start,
                                                       end=self.expire))
        return rstring


class TooManyKeys(Exception):
    pass


class Server:
    def __init__(self, serverurl):
        self.serverurl = Server.sanitize(serverurl)
        self.lookupurl = self.serverurl + "pks/lookup"

    @classmethod
    def sanitize(self, serverurl):
        serverurl = serverurl.strip()

        if(serverurl.startswith("hkp://")):
            serverurl.replace("hkp", "http", 1)
        if not serverurl.startswith("http"):
            serverurl = "http://" + serverurl
        if not serverurl.endswith("/"):
            serverurl = serverurl + "/"

        return serverurl

    def get(self, pattern):
        payload = {"op": "get", "search": "0x" + pattern, "options": "mr"}
        r = requests.get(self.lookupurl, verify=True, params=payload)
        print(r.text)

    def index(self, pattern):
        payload = {"op": "index", "search": pattern, "options": "mr"}
        r = requests.get(self.lookupurl, verify=True, params=payload)

        # No keys found
        if(r.status_code == 404):
            return None
        elif(r.status_code == 500):
            raise TooManyKeys("Too many keys")
        elif(r.status_code == 200):
            text = r.text.split("\n", 1)[1].strip()
            keylist = []
            key_text = text.split("pub:")[1:]
            for key in key_text:
                pub, *uids = key.strip().split("\n")
                pub = pub.strip().split(":")
                final_uids = []
                for uid in uids:
                    uid = uid.strip().split(":")
                    if(uid[0] == "uid"):
                        final_uids.append(tuple(uid[1:]))

                finalkey = Key(pub, final_uids)
                keylist.append(finalkey)
            return keylist

        else:
            print(r)
            raise Exception("Unknown Error")

    def getchoice(self, keys):
        for sno, key in enumerate(keys):
            print("({number}) {key}".format(number=sno+1, key=str(key)))

        while(True):
            try:
                choices = map(int, input("Enter your choice > ").strip().split())
                break
            except EOFError:
                return None
            except ValueError:
                print("Please Enter valid choices")
            
        for number in choices:
            if number < len(keys) and number >= 1:
                self.get(keys[number-1].fpr)


if __name__ == "__main__":
    server = Server("pgp.mit.edu")
    searchstr = input("enter a recipient to search> ")
    keys = server.index(searchstr)

    if(keys in [None, []]):
        print("No keys found")
    else:
        server.getchoice(keys)
