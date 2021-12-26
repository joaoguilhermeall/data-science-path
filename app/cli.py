from getpass import getpass
from os import environ
from re import S
from typing import Union, Dict

from pathlib import Path
from json import loads
import argparse

from app.config import AppConfig
from app.exceptions import KaggleKeysEnviron, KaggleKeysFile


class CLI:
    def __init__(self, configs: AppConfig = None) -> None:
        self._configs = configs if configs is not None else AppConfig()

        self._build_cli()
        self._run_cli()

    def _build_cli(self) -> None:
        """Build all CLI options"""

        self._parser = argparse.ArgumentParser(
            prog="APP",
            description="Lucas's Data Science Path with Pima Indians Diabetes Database",
            epilog="That's all, folks!\n",
        )

        self._parser.add_argument(
            "level",
            choices=["extract", "transform", "load", "pipeline"],
            help="Application level to run",
        )

        self._parser.add_argument(
            "--force",
            "-f",
            help="Force download dataset from Kaggle",
            action="store_true",
        )

        self._parser.parse_args()

    def _run_cli(self) -> None:
        if self.args.force:
            self._configs.KAGGLE_DOWNLOAD_FORCE = True

        if (
            not self.configs.KAGGLE_DATASET_FILE.exists()
            or self.args.force
        ):
            credentials = {}

            credentials = self._get_kaggle_credentials()

            self._export_kaggle_credentials(credentials)

    @property
    def args(self) -> argparse.Namespace:
        """Return parseds arguments"""
        return self._parser.parse_args()

    @property
    def configs(self) -> AppConfig:
        return self._configs

    @property
    def level(self) -> str:
        return self.args.level

    @property
    def verbose(self) -> str:
        return self.args.verbose

    def _get_kaggle_credentials_from_environ(self) -> Dict[str, str]:
        credentials = {}

        try:
            credentials["KAGGLE_USERNAME"] = environ["KAGGLE_USERNAME"]
            credentials["KAGGLE_KEY"] = environ["KAGGLE_KEY"]

        except KeyError as ke:
            msg = " ".join(
                [
                    "There is no variables seted on environ.",
                    f"Following key is resquest: {ke}.",
                    "See how to run app on README file.",
                ]
            )
            print(KaggleKeysEnviron(msg))

        return credentials

    def _get_kaggle_credentials_from_file(self) -> Dict[str, str]:
        """Check if credential file API exists"""
        credentials = {}
        credentials_file = Path(self._configs.KEYS) / "kaggle.json"

        if credentials_file.exists():
            with open(credentials_file) as file:
                credentials_dict = loads(file.read())

            try:
                credentials["KAGGLE_USERNAME"] = credentials_dict["username"]
                credentials["KAGGLE_KEY"] = credentials_dict["key"]

            except KeyError as ke:
                msg = " ".join(
                    [
                        "There is no valid kaggle.json file on keys folder.",
                        f"Following key is resquest: {ke}.",
                        "See how to run app on README file or by options invoking [-h] flag.",
                    ]
                )
                print(KaggleKeysFile(msg))

        return credentials

    def _get_kaggle_credentials(self) -> Dict[str, str]:
        credentials = self._get_kaggle_credentials_from_environ()

        if credentials == {}:
            credentials = self._get_kaggle_credentials_from_file()

        if credentials == {}:
            credentials = self._request_kaggle_credentials()

        return credentials

    def _request_kaggle_credentials(self) -> Dict[str, str]:
        """Request KAGGLE credentials"""

        print("\nKaggle Credentials\n")
        print("Credentials are being requested because the", end=" ")
        print("configuration file was not found and the variables", end=" ")
        print("were not found in the environment", end="\n\n")

        credentials = {}

        credentials["KAGGLE_USERNAME"] = input("Enter Kaggle API Username: ")
        credentials["KAGGLE_KEY"] = getpass("Enter Kaggle API Key: ")

        print()

        return credentials

    def _export_kaggle_credentials(self, credentials: Dict[str, str]) -> None:
        """Export kaggle credentials to environ"""
        environ["KAGGLE_USERNAME"] = credentials["KAGGLE_USERNAME"]
        environ["KAGGLE_KEY"] = credentials["KAGGLE_KEY"]

        self._configs.KAGGLE_USERNAME = credentials["KAGGLE_USERNAME"]
        self._configs.KAGGLE_KEY = credentials["KAGGLE_KEY"]


if __name__ == "__main__":
    pass
