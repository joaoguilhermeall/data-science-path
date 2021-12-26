from app.cli import CLI
from app.etl import ETL
from app.config import AppConfig


class App(object):
    """App abstracion class"""
    
    def __init__(self) -> None:
        self._configs = AppConfig()
        self._cli = None
        self._etl = None

    @property
    def configs(self) -> AppConfig:
        return self._configs
    
    @property
    def cli(self) -> CLI:
        if self._cli == None:
            self._cli = CLI(self.configs)

        return self._cli

    @property
    def etl(self) -> ETL:
        if self._etl == None:
            self._etl = ETL(self.configs)
        
        return self._etl
    
    def run(self):
        """Run App - Callable only by terminal enviroment"""
        level = self.etl[self.cli.level]
        level()



