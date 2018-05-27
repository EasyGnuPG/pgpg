# pgpg

Implementation of EasyGnuPG with Python and GPGME.

## Developer Installation

```bash
apt-get install python3-pip python3-gpg
pip3 install virtualenv
git clone https://github.com/EasyGnuPG/pgpg
virtualenv --python=python3 python3venv
source ./python3venv/bin/activate # activate virtual environment
cd pgpg
pip3 install --editable .
# One should develop and test pgpg in virtualenv only
# When you are done with the testing use:
deactivate
# you can get back into the virtual env by activating it again (line 4)
```

You can use [pgpg-ds](https://github.com/EasyGnuPG/pgpg-ds) also.

## User Installation

__pgpg__ is in developement stage and not ready for user installation yet
