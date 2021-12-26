from os import path

from pathlib import Path
from abc import ABC

import src


class _BaseConfig(ABC):
    APP_PATH = Path(path.dirname(src.__file__))
    OUTPUT = APP_PATH / "../output"
    INPUT = APP_PATH / "../input"
    KEYS = APP_PATH / "../keys"

    KAGGLE_DOWNLOAD_FORCE = False

    KAGGLE_USERNAME = None
    KAGGLE_KEY = None

    KAGGLE_DATASET = "uciml/pima-indians-diabetes-database"
    KAGGLE_DATASET_PATH = INPUT / "pima-indians-diabetes-database.zip"

    KAGGLE_URI = "https://www.kaggle.com/"


class AppConfig(_BaseConfig):
    """Application Configuration and ​​Execution Variables"""
    pass

