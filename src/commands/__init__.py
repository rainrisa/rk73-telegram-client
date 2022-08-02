from glob import glob
from os.path import basename, dirname, isfile


def get_all_commands():
    fn_path = glob(dirname(__file__) + "/*.py")

    all_commands = [
        basename(f)[:-3]
        for f in fn_path
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")
    ]
    return all_commands


ALL_COMMANDS = sorted(get_all_commands())
__all__ = ALL_COMMANDS + ["ALL_MODULES"]
