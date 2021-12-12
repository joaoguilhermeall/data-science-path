import argparse


def cli_constructor() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        prog="Data Science Path - CLI",
        description="Run a specific routines of Pipeline Application",
    )

    parser.add_argument(
        "action",
        choices=["extract", "transform", "load", "pipeline"],
        help="Level of Application",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Be verbose",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--kaggle",
        help="Require Username and API Key of Kaggle if dataset was not downloaded yet",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-f",
        "--force",
        help="Force Kaggle Request credentials and download dataset even if it already exists",
        action="store_true",
        default=False,
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    cli_constructor()
