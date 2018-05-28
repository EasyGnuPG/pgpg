import click


@click.command()
def cmd_generate():
    """
    Create a new GPG key. If email and name are not given as arguments,
    they will be asked interactively.
    """
    raise NotImplementedError