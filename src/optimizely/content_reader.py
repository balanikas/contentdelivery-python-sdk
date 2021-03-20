import requests
import logging
import json

from requests import exceptions as requests_exceptions

from src.optimizely.entities import Site, Content
from src.optimizely.exceptions import SiteNotFoundException


class ContentReader:
    def __init__(self, host, logger):
        self.host = host
        self.logger = logger

    def get_single(self, id=""):
        try:
            url = self.host + "/content/" + id
            response = requests.get(url)
        except requests_exceptions.RequestException as error:
            self.logger.error(error)
            return None

        if not response:
            self.logger.error("{0} returned {1}".format(url, response.status_code))
            return None

        return self._handle_response(response)

    def _handle_response(self, response):
        return Content(response.json())
