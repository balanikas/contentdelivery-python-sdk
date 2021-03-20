import logging

from src.optimizely.content_reader import ContentReader
from src.optimizely.sites_reader import SitesReader


class Optimizely(object):

    def __init__(
            self,
            host,
            logger):
        self.host = host
        self.logger = logger or logging
        self.sites = SitesReader(host, logger)
        self.content = ContentReader(host, logger)



