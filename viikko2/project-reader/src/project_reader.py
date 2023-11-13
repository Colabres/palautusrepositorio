from urllib import request
from project import Project
import toml



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)
        poetrydata = data["tool"]["poetry"]
        #print(content)
        #print(poetrydata)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(poetrydata["name"], poetrydata["description"], poetrydata["dependencies"], poetrydata["group"]["dev"]["dependencies"],poetrydata["license"],poetrydata["authors"])
