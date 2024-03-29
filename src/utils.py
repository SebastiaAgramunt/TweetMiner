import os
from pathlib import Path


def create_dirs(*paths):
    """
    Creates a set of directories from a tuple of directories
    :param paths: List or tuple of strings for the paths to be created if they do not exist
    :return: void
    """
    for path in paths:

        if not os.path.exists(path):
            os.mkdir(path)


def project_abs_path():
    return Path(__file__).parent.parent.parent