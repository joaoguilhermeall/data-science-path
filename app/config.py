from os import environ
from getpass import getpass

from pathlib import Path
from abc import ABC

class KaggleException(BaseException):
    """There is some variable api not founded on environ"""
    pass


class _BaseConfig(ABC):
    OUTPUT = Path("../output")
    DOWNLOAD = Path("../download")

    REQUEST_KAGGLE = False

    KAGGLE_USERNAME = ""
    KAGGLE_KEY = ""

    API_KAGGLE_KEY = "kaggle datasets download -d uciml/pima-indians-diabetes-database"

class BaseConfig(_BaseConfig):
    pass

class Config(_BaseConfig):
    def __init__(self) -> None:
        super().__init__()
        try:
            KAGGLE_USERNAME = environ['KAGGLE_USERNAME']
            KAGGLE_KEY = environ['KAGGLE_KEY']
        except KeyError as ke:
            raise(KaggleException(f"The follow environ variable need to be export or set: {ke}"))


class ConfigKaggle(_BaseConfig):
    def __init__(self) -> None:
        super().__init__()
        if _BaseConfig.KAGGLE_USERNAME == "":
            KAGGLE_USERNAME = input("Enter Kaggle API Username: ")
            environ['KAGGLE_USERNAME'] = KAGGLE_USERNAME
        
        if _BaseConfig.KAGGLE_KEY == "":
            KAGGLE_KEY = getpass("Enter Kaggle API Key: ")
            environ['KAGGLE_KEY'] = KAGGLE_KEY