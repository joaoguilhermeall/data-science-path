from argparse import Namespace

from app.etl import ETL
from app.config import Config, ConfigKaggle

def run_app(args: Namespace) -> int:
    
    # Config parameters
    config = None

    if args.kaggle:
        config = ConfigKaggle()
    else:
        config = Config()

    # Run action called
    etl = ETL(config)
    action = etl[args.action]
    action()

    return 0