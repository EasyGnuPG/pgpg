import click

from pgpg.contact.cmd.list import cmd_list
from pgpg.contact.cmd.delete import cmd_delete
from pgpg.contact.cmd.export import cmd_export
from pgpg.contact.cmd.add import cmd_add
from pgpg.contact.cmd.fetch import cmd_fetch
from pgpg.contact.cmd.fetch_uri import cmd_fetch_uri
from pgpg.contact.cmd.search import cmd_search
from pgpg.contact.cmd.receive import cmd_receive
from pgpg.contact.cmd.certify import cmd_certify
from pgpg.contact.cmd.uncertify import cmd_uncertify
from pgpg.contact.cmd.trust import cmd_trust

@click.group()
def cmd_contact():
    """
    Commands for handling the contacts. For more details see contact help.
    """
    raise NotImplementedError

cmd_contact.add_command(cmd_list,"list")
cmd_contact.add_command(cmd_delete,"delete")
cmd_contact.add_command(cmd_export,"export")
cmd_contact.add_command(cmd_add,"add")
cmd_contact.add_command(cmd_fetch,"fetch")
cmd_contact.add_command(cmd_fetch_uri,"fetch-uri")
cmd_contact.add_command(cmd_search,"search")
cmd_contact.add_command(cmd_receive,"receive")
cmd_contact.add_command(cmd_certify,"certify")
cmd_contact.add_command(cmd_uncertify,"uncertify")
cmd_contact.add_command(cmd_trust,"trust")
