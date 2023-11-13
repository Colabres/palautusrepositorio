class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, myLisence, myAutors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.licence = myLisence
        self.autors = myAutors

    def _stringify_dependencies(self, dependencies):
        return "\n -  ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.licence}"
            f"\n"
            f"\nAutors:\n -  {self._stringify_dependencies(self.autors)}"
            f"\n"
            f"\nDependencies:\n -  {self._stringify_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:\n -  {self._stringify_dependencies(self.dev_dependencies)}"
            

        )
