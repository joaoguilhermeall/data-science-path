from pathlib import Path
from typing import Any, Dict, List, Union

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
        self._dataframes: Dict[str, DataFrame] = {}

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

    def _download_dataset(self, dataset: str, filename: str) -> Path:
        """Download dataset file from Kaggle"""
        # Import from method because KaggleApi is instantiated when It is called
        from kaggle.api.kaggle_api_extended import KaggleApi, ApiException

        kaggle_api = KaggleApi()
        kaggle_api.authenticate()

        try:
            kaggle_api.dataset_download_file(
                dataset=dataset,
                file_name=filename,
                path=self._configs.INPUT,
                force=True,
                quiet=False
            )
        except ApiException(401) as ex:
            raise (
                KaggleException(f"{ex}: Please, try a new Kaggle API Token. Manages it on the kaggle website")
            )
        
        return self._configs.KAGGLE_DATASET_FILE

    def extract(self) -> None:
        """Extract and build information"""
        dataset = self._configs.KAGGLE_DATASET
        filename = self._configs.KAGGLE_DATASET_FILENAME
        file_key = filename.name.rsplit(".")[0]

        # If dataset file not exist or force download
        if not self._configs.KAGGLE_DATASET_FILE.exists():
            verbose("File does not exist. Downloading")
            file_path = self._download_dataset(dataset, filename)
            
        elif self._configs.KAGGLE_DOWNLOAD_FORCE:
            verbose("Force download!")
            file_path = self._download_dataset(dataset, filename)
        else:
            pass

        self._dataframes[file_key] = read_csv(file_path)

    def transform(self):
        pass

    def loading(self):
        pass

    def pipeline(self):

        self.extract()
        self.transform()
        self.loading()

    def dataframe(self) -> Union[DataFrame, None]:
        return self._dataframes
