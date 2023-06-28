import json
import logging

import click
from flask import Flask

from .load_data import load_data_from_file

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger("flask-app")
logger.setLevel(logging.ERROR)
cv_data = {}
VALID_URL_ROUTES = []


def setup():
    """
    This function is used to verify that data has been correctly loaded. In case
    of failure, the app will exit with code -1.
    """
    global cv_data
    global VALID_URL_ROUTES
    cv_data = load_data_from_file()
    if not cv_data:
        logger.critical("Couldn't load cv data. Exiting")
        exit(-1)
    VALID_URL_ROUTES = list(cv_data.keys())


setup()


@app.route("/")
def empty_route():
    """
    This route handles the empty route and provides a brief presentation of
    the website
    """
    available_routes = " ".join(["<br>/" + route for route in VALID_URL_ROUTES])
    welcome_string = (
        "Welcome to Luca Manea's presentation site.<br>" + "Available routes:"
    )
    return welcome_string + available_routes


@app.cli.command("present-cv")
@click.argument("route")
def main_route_cli(route):
    """
    This route handles CLI commands. It checks for valid routes and provides CV
    data in a pretty-ed, indented manner.
    :param route: CV filed to be presented
    """
    if route in VALID_URL_ROUTES:
        logger.info("Accessed CLI via route: {}".format(route))
        return click.echo(json.dumps(cv_data[route], indent=2))
    else:
        logger.warning("Invalid route")
        click.echo("Sorry, invalid route!")


@app.route("/<route>")
def main_route_rest(route):
    """
        Main route which checks that all connections to the site are valid
    routes.
    :param route: CV filed to be returned as JSON
    :return:
    """

    if route in VALID_URL_ROUTES:
        logger.info("Accessed REST API via route: {}".format(route))
        return cv_data[route]
    else:
        logger.warning("Invalid route")
        return "Sorry, invalid route"


if __name__ == "__main__":
    app.run()
