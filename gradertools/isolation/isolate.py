from .isolate_isolate import IsolateIsolate


class Isolate:
    def __init__(self, isolator=None):
        if isolator is None:
            isolator = 'isolate'
        if isolator == 'isolate':
            Isolator = IsolateIsolate
        else:
            raise Exception('Unknown Isolator')

        self._isol = Isolator('isolate')

    def isolate(self, command, files=None, parameters=None, envvariables=None, directories=None, allowmultiprocess=None):
        if files is None:
            files=[]
        if parameters is None:
            parameters=[]
        if envvariables is None:
            envvariables=[]
        if directories is None:
            directories = []
        if allowmultiprocess is None:
            allowmultiprocess=False
        return self._isol.isolate(files, command, parameters, envvariables, directories, allowmultiprocess)

    def clean(self):
        self._isol.clean()
