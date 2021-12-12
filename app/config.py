from os import environ, path
from getpass import getpass

from pathlib import Path
from abc import ABC

import app


class KaggleException(BaseException):
    """There is some variable api not founded on environ"""

    pass


class _BaseConfig(ABC):
    APP_PATH = Path(path.dirname(app.__file__))
    OUTPUT = APP_PATH / "../output"
    DOWNLOAD = APP_PATH / "../download"
    REQUEST_KAGGLE = False
    REQUEST_KAGGLE_FORCE = False

    KAGGLE_USERNAME = ""
    KAGGLE_KEY = ""

    KAGGLE_DATASET = "uciml/pima-indians-diabetes-database"
    KAGGLE_DATASET_FILENAME = "diabetes.csv"


class BaseConfig(_BaseConfig):
    pass


class Config(_BaseConfig):
    def __init__(self) -> None:
        super().__init__()
        try:
            self.KAGGLE_USERNAME = environ["KAGGLE_USERNAME"]
            self.KAGGLE_KEY = environ["KAGGLE_KEY"]
        except KeyError as ke:
            msg = " ".join(
                [
                    f"The follow environ variable need to be export or set: {ke}.",
                    "See how to run app on README file.",
                ]
            )
            raise (KaggleException(msg))


class ConfigKaggle(_BaseConfig):
    def __init__(self, force: bool = False) -> None:
        _BaseConfig.REQUEST_KAGGLE = True
        _BaseConfig.REQUEST_KAGGLE_FORCE = force

        super().__init__()

        if (
            self.REQUEST_KAGGLE
            and not path.exists(self.DOWNLOAD / self.KAGGLE_DATASET_FILENAME)
            or self.REQUEST_KAGGLE_FORCE
        ):
            # Request KAGGLE credentials
            print("Kaggle Credentials\n")

            self.KAGGLE_USERNAME = input("Enter Kaggle API Username: ")
            environ["KAGGLE_USERNAME"] = self.KAGGLE_USERNAME

            self.KAGGLE_KEY = getpass("Enter Kaggle API Key: ")
            environ["KAGGLE_KEY"] = self.KAGGLE_KEY
