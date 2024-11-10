class Project:
    def __init__(self, name, description, authors, dependencies, dev_dependencies):
        self.name = name
        self.authors = authors
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "".join([f"\n- {dep}" for dep in dependencies])

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nAuthors: {self._stringify_dependencies(self.authors)}"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
