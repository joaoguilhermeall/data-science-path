import logging
from re import VERBOSE

VERBOSE = 25


def verbose(msg: str) -> None:
    """Verbose execution

    Args:
        msg (str): Message to show on verbose
    """
    logging.log(msg, VERBOSE)


class Logger:
    """Define a Logger constructor"""

    def __init__(self, level: int = logging.WARNING, verbose: bool = False) -> None:
        if verbose:
            logging.addLevelName(VERBOSE, "VERBOSE")

        self._formatter = logging.Formatter()
        self._logger = logging.getLogger(name="Data Science Path - Logger")

    def run(level: int = logging.DEBUG) -> None:
        pass
