from urllib import request
from project import Project
import tomllib as toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content = toml.loads(content)
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Ohtutesting app", "Sovellus joka toimii testisyötteenä ohtun osan 2 laskareihin", "MIT", "\n- Matti Luukkainen \n- Kalle Ilves", ["\n- python\n- Flask\n- editdistance"], ["\n- coverage\n- robotframework\n- robotframework-seleniumlibrary\n- requests"])