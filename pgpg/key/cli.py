import click

from pgpg.key.cmd.list import cmd_list
from pgpg.key.cmd.generate import cmd_generate
from pgpg.key.cmd.fetch import cmd_fetch
from pgpg.key.cmd.backup import cmd_backup
from pgpg.key.cmd.restore import cmd_restore
from pgpg.key.cmd.split import cmd_split
from pgpg.key.cmd.join import cmd_join
from pgpg.key.cmd.recover import cmd_recover
from pgpg.key.cmd.passphrase import cmd_passphrase
from pgpg.key.cmd.share import cmd_share
from pgpg.key.cmd.renew import cmd_renew
from pgpg.key.cmd.revcert import cmd_revcert
from pgpg.key.cmd.revoke import cmd_revoke
from pgpg.key.cmd.delete import cmd_delete

@click.group()
def cmd_key():
    """
    Commands for handling the key. For more details see key help
    """
    raise NotImplementedError

cmd_key.add_command(cmd_list,"list")
cmd_key.add_command(cmd_generate,"generate")
cmd_key.add_command(cmd_fetch,"fetch")
cmd_key.add_command(cmd_backup,"backup")
cmd_key.add_command(cmd_restore,"restore")
cmd_key.add_command(cmd_split,"split")
cmd_key.add_command(cmd_join,"join")
cmd_key.add_command(cmd_recover,"recover")
cmd_key.add_command(cmd_passphrase,"pass")
cmd_key.add_command(cmd_share,"share")
cmd_key.add_command(cmd_renew,"renew")
cmd_key.add_command(cmd_revcert,"revcert")
cmd_key.add_command(cmd_revoke,"revoke")
cmd_key.add_command(cmd_delete,"delete")