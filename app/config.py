from os import environ, path
from getpass import getpass
from json import loads

from pathlib import Path
from abc import ABC
from typing import Dict, Union

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


class ConfigApp(_BaseConfig):
    def __init__(self, force: bool = False) -> None:
        BaseConfig.REQUEST_KAGGLE_FORCE = force

        try:
            self.KAGGLE_USERNAME = environ["KAGGLE_USERNAME"]
            self.KAGGLE_KEY = environ["KAGGLE_KEY"]
        except KeyError as ke:
            credentials = {}
            credentials = ConfigApp.check_kaggle_credentials()
            
            if not credentials:
                credentials = ConfigApp.request_kaggle_credentials()
            
            ConfigApp.export_kaggle_credentials(credentials)

    @staticmethod
    def check_kaggle_credentials() -> Union[None, Dict[str, str]]:
        """Check if credential file API exists"""
        credentials = {}
        credentials_file = Path(BaseConfig.APP_PATH) / "../keys/kaggle.json"

        if credentials_file.exists():
            with open(credentials_file) as file:
                credentials_dict = loads(file.read())

            try:
                credentials = {}
                credentials["KAGGLE_USERNAME"] = credentials_dict["username"]
                credentials["KAGGLE_KEY"] = credentials_dict["key"]
            except KeyError as ke:
                msg = " ".join(
                    [
                        f"The kaggle.json file need following key: {ke}.",
                        "See how to run app on README file.",
                    ]
                )
                print(KaggleException(msg))
                return None

        return credentials

    @staticmethod
    def request_kaggle_credentials() -> Dict[str, str]:
        """Request KAGGLE credentials"""

        print("Kaggle Credentials\n")
        credentials = {}

        credentials["KAGGLE_USERNAME"] = input("Enter Kaggle API Username: ")
        credentials["KAGGLE_KEY"] = getpass("Enter Kaggle API Key: ")

        return credentials
    
    @staticmethod
    def export_kaggle_credentials(credentials: Dict[str, str]) -> None:
        """Export kaggle credentials to environ"""
        environ["KAGGLE_USERNAME"] = credentials["KAGGLE_USERNAME"]
        environ["KAGGLE_KEY"] = credentials["KAGGLE_KEY"]

        BaseConfig.KAGGLE_USERNAME = credentials["KAGGLE_USERNAME"]
        BaseConfig.KAGGLE_KEY = credentials["KAGGLE_KEY"]

