import click

from pgpg.core.cmd.init import cmd_init
from pgpg.core.cmd.migrate import cmd_migrate
from pgpg.core.cmd.info import cmd_info
from pgpg.core.cmd.seal import cmd_seal
from pgpg.core.cmd.open import cmd_open
from pgpg.core.cmd.sign import cmd_sign
from pgpg.core.cmd.verify import cmd_verify
from pgpg.core.cmd.set import cmd_set
from pgpg.core.cmd.gpg import cmd_gpg
from pgpg.core.cmd.default import cmd_default