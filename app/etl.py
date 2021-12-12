from typing import Any

from abc import ABC

from app.logger import verbose
from app.config import BaseConfig


class ActionETLException(BaseException):
    pass


class ETL(ABC):
    """Base ETL class"""

    def __init__(self, configs: BaseConfig) -> None:
        super().__init__()
        self._configs = configs

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

    def extract(self):
        # TODO: Build extract dataset from kaggle
        from kaggle.api.kaggle_api_extended import KaggleApi

        #kaggle.api.authenticate()

        pass

    def transform(self):
        pass

    def loading(self):
        pass

    def pipeline(self):

        self.extract()
        self.transform()
        self.loading()
