from typing import Any, Union

import os
from abc import ABC

from pandas import DataFrame, read_csv

from app.logger import verbose
from app.config import BaseConfig, KaggleException


class ActionETLException(BaseException):
    pass


class ETL(ABC):
    """Base ETL class"""

    def __init__(self, configs: BaseConfig) -> None:
        super().__init__()
        self._configs = configs
        self._dataframe = None

    def __getitem__(self, name: str) -> Any:
        if name == "extract":
            return self.extract
        elif name == "transform":
            return self.transform
        elif name == "loading":
            return self.loading
        elif name == "pipeline":
            return self.pipeline
        else:
            raise (ActionETLException(f"Action for ETL is not valid: {name}"))

    def extract(self) -> None:
        """Download dataset file"""
        if (
            not os.path.exists(self._configs.KAGGLE_DATASET_FILE)
            or self._configs.REQUEST_KAGGLE_FORCE
        ):

            from kaggle.api.kaggle_api_extended import KaggleApi, ApiException

            kaggle_api = KaggleApi()
            kaggle_api.authenticate()

            try:
                kaggle_api.dataset_download_file(
                    self._configs.KAGGLE_DATASET,
                    self._configs.KAGGLE_DATASET_FILENAME,
                    path=self._configs.DOWNLOAD,
                    force=self._configs.REQUEST_KAGGLE_FORCE,
                    quiet=False
                )
            except ApiException(401) as ex:
                raise (
                    KaggleException(f"{ex}: Please, try a new Kaggle API Token. Manages it on the kaggle website")
                )
            
        self._dataframe = read_csv(self._configs.KAGGLE_DATASET_FILE)

    def transform(self):
        pass

    def loading(self):
        pass

    def pipeline(self):

        self.extract()
        self.transform()
        self.loading()

    def dataframe(self) -> Union[DataFrame, None]:
        return self._dataframe
