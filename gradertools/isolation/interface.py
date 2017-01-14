class IsolateInterface:
    def __init__(self, isolator):
        self.isolator = isolator

    def isolate(self, files, command, parameters, envvariables, directories, allowmultiprocess):
        raise NotImplementedError

    def clean(self):
        raise NotImplementedError
