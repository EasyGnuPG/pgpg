import click


@click.command()
def cmd_list():
    """
    Show  the details of the contacts (optionally in raw format or with
    colons). A list of all the contacts will be displayed if no one  is
    selected. A contact can be selected by name, email, id, etc.
    """
    raise NotImplementedError