import click

from pgpg.core.cli import (cmd_init, cmd_migrate, cmd_info, cmd_seal, 
    cmd_open, cmd_sign, cmd_verify, cmd_set, cmd_gpg)

from pgpg.key.cli import cmd_key

from pgpg.contact.cli import cmd_contact


@click.group()
def main():
    """
    There  are  scads  of options presented by GnuPG, which are all part of
    making it the flexible and powerful an encryption framework that it is.
    But it´s extremely complicated to get started with, and that quite rea‐
    sonably puts people off.

    pgpg is a wrapper script that tries to simplify the  process  of  using
    GnuPG. In order to simplify things, it is opinionated about the "right"
    way to use GnuPG.
    """

main.add_command(cmd_init,"init")
main.add_command(cmd_migrate,"migrate")
main.add_command(cmd_info,"info")
main.add_command(cmd_seal,"seal")
main.add_command(cmd_open,"open")
main.add_command(cmd_sign,"sign")
main.add_command(cmd_verify,"verify")
main.add_command(cmd_set,"set")
main.add_command(cmd_key,"key")
main.add_command(cmd_contact,"contact")
main.add_command(cmd_gpg,"gpg")