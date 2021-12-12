from app.cli import cli_constructor
from app.run import run_app

# Call CLI constructor
args = cli_constructor()

run_app(args)