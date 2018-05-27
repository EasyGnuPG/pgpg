import click


@click.command()
def cmd_renew():
    """
    Renew the key until the given date (by default 1 month  from  now).
    The  date  is  in  free  time  format, like "2 months", 2020-11-15,
    "March 7", "5 years" etc. The  date  formats  are  those  that  are
    accepted by the command date -d (see info date).
    """
    raise NotImplementedError