import click


@click.command()
def cmd_list():
    """
    Show  the  details  of  the  key  (optionally in raw format or with
    colons). A list of all the keys can be displayed as well (including
    the revoked and expired ones).
    """
    raise NotImplementedError