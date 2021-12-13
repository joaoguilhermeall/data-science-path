from argparse import Namespace

from app.etl import ETL
from app.config import ConfigApp

def run_app(args: Namespace) -> int:
    
    # Config parameters
    config = None

    config = ConfigApp()

    # Run action called
    etl = ETL(config)
    action = etl[args.action]
    action()

    return 0