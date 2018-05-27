import click


@click.command()
def cmd_fetch():
    """
    Get a key from another gpg directory (by default from $GNUPGHOME).
    """
    raise NotImplementedError