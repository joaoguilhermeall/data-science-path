import argparse


def cli_constructor() -> None:

    parser = argparse.ArgumentParser(prog="App CLI")
    
    parser.add_argument(
        "level",
        choices=["extract", "transform", "load", "pipeline"],
        help="Level of Application",
    )

    args = parser.parse_args()


if __name__ == "__main__":
    ...
