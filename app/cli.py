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
        help="Require Username and API Key of Kaggle from prompt",
        action="store_true",
        default=False,
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    cli_constructor()
