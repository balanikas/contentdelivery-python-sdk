from typing import List
import json


class Language(object):
    def __init__(self, data):
        self.name = data.get("name")
        self.display_name = data.get("displayName")
        self.is_master_language = data.get("isMasterLanguage")


class Site(object):
    def __init__(self, data):
        self.name = data.get("name")
        self.id = data.get("id")
        self.languages = [Language(l) for l in data.get("languages", [])]


class Content(object):
    def __init__(self, data):
        self.name = data.get("name")
        self.id = data["contentLink"]["id"]