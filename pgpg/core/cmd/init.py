import click

@click.command()
def cmd_init():
    """
    Initialize egpg. Optionally give the directory to be used.  If  not
    given, the default directory will be $HOME/.egpg/
    """
    raise NotImplementedError