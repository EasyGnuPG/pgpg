import click


@click.command()
def cmd_split():
    """
    Split the key into 3 partial keys and store one of them on the don‐
    gle (removable device, usb), keep the other one  locally,  and  use
    the third one as a backup. Afterwards, whenever the key needs to be
    used, the dongle has to be present.
    """
    raise NotImplementedError