#!/usr/bin/env python
"""Command-line interface."""
import click
from rich import traceback


@click.command()
@click.version_option(version="0.1.0", message=click.style("historic-weather-forecast Version: 0.1.0"))
def main() -> None:
    """historic-weather-forecast."""


if __name__ == "__main__":
    traceback.install()
    main(prog_name="historic-weather-forecast")  # pragma: no cover
