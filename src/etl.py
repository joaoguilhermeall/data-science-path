from pathlib import Path
from typing import Any, Callable, Dict, Union

from abc import ABC
import zipfile

from pandas import DataFrame, read_csv

from src.logger import verbose
from src.config import AppConfig

from src.exceptions import KaggleTokenInvalid, LevelETLException


class ETL(ABC):
    """Base ETL class"""

    def __init__(self, configs: AppConfig = None) -> None:
        super().__init__()
        self._configs = configs if configs is not None else AppConfig()
        self._dataframes: Dict[str, DataFrame] = {}

    def __getitem__(self, name: str) -> Callable[[], None]:
        if name == "extract":
            return self.extract
        elif name == "transform":
            return self.transform
        elif name == "loading":
            return self.loading
        elif name == "pipeline":
            return self.pipeline
        else:
            raise (LevelETLException(f"ETL level is not valid: {name}"))

    def _download_dataset(self, dataset: str, force: str = False) -> None:
        """Download dataset file from Kaggle"""
        # Import from method because KaggleApi is instantiated when It is called
        from kaggle.api.kaggle_api_extended import KaggleApi, ApiException

        kaggle_api = KaggleApi()
        kaggle_api.authenticate()

        try:
            kaggle_api.dataset_download_files(
                dataset=dataset,
                path=self.input_fd,
                force=force,
                quiet=False,
                unzip=False
            )
        except ApiException(401) as ex:
            raise (
                KaggleTokenInvalid(f"{ex}: Please, try a new Kaggle API Token. Manages it on the kaggle website")
            )

    def extract(self) -> None:
        """Extract and build information"""
        dataset = self._configs.KAGGLE_DATASET
        
        # If dataset file not exist or force download
        if not self.dataset_path.exists():
            self._download_dataset(dataset)
            
        elif self._configs.KAGGLE_DOWNLOAD_FORCE:
            self._download_dataset(dataset, True)
        
        # If necessary, build another Dataframes here
        with zipfile.ZipFile(self.dataset_path) as file_ziped:
            for file in file_ziped.filelist:
                if file.filename.endswith(".csv"):
                    with file_ziped.open(file) as csv_ziped:
                        # Add dataframe
                        self._dataframes[csv_ziped.name] = read_csv(csv_ziped)

    def transform(self):
        # TODO: ETL TRANSFORM
        pass

    def loading(self):
        # TODO: ETL LOADING
        pass

    def pipeline(self):
        """Run all steps of ETL"""
        self.extract()
        self.transform()
        self.loading()

    @property
    def dataframes(self) -> Union[DataFrame, None]:
        return self._dataframes

    @property
    def input_fd(self) -> Path:
        """Input Folder"""
        return self._configs.INPUT
    
    @property
    def output_fd(self) -> Path:
        """Output Folder"""
        return self._configs.OUTPUT

    @property
    def dataset_path(self) -> Path:
        return self._configs.KAGGLE_DATASET_PATH