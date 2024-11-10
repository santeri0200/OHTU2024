from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_content = toml.loads(content)
        poetry_content = parsed_content["tool"]["poetry"]

        name     = poetry_content["name"]
        desc     = poetry_content["description"]
        license  = poetry_content["license"]
        authors  = poetry_content["authors"]
        deps     = poetry_content["dependencies"]
        dev_deps = poetry_content["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, authors, deps, dev_deps)
