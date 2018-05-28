import click


@click.command()
def cmd_backup():
    """
    Backup key to text file. If the option --qrencode is given, then  a
    PDF file with 3D barcode will be generated as well.
    """
    raise NotImplementedError