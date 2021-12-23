from abc import ABC

from app.cli import CLI
from app.etl import ETL
from app.config import AppConfig


class App(ABC):
    def __init__(self) -> None:
        configs = AppConfig()

        self.cli(CLI(configs))
        self.etl(ETL(configs))
        self.configs(configs)

    @property
    def configs(self) -> AppConfig:
        return self._configs
    
    @configs.setter
    def configs(self, configs: AppConfig) -> None:
        self._configs = configs
    
    @property
    def cli(self) -> CLI:
        return self._cli

    @cli.setter
    def cli(self, cli: CLI) -> None:
        self._cli = cli

    @property
    def etl(self) -> ETL:
        return self._etl
    
    @etl.setter
    def etl(self, etl: ETL) -> None:
        self._etl = etl
    
    def run(self):
        """Run App"""
        level = self._etl[self._cli.level]
        level()



