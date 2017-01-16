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

    def isolate(self, command, files=None, parameters=None, envvariables=None, directories=None,
                allowmultiprocess=None, stdinfile=None, stdoutfile=None):
        if files is None:
            files = []
        if parameters is None:
            parameters = []
        if envvariables is None:
            envvariables = []
        if directories is None:
            directories = []
        if allowmultiprocess is None:
            allowmultiprocess = False
        return self._isol.isolate(files, command, parameters, envvariables, directories, allowmultiprocess, stdinfile,
                                  stdoutfile)

    def clean(self):
        self._isol.clean()

    @property
    def status(self):
        return self._isol.get_status()

    @property
    def boxdir(self):
        return self._isol.get_boxdir()

    @property
    def time(self):
        return self._isol.get_time()

    @property
    def walltime(self):
        return self._isol.get_walltime()

    @property
    def maxrss(self):
        return self._isol.get_maxrss()

    @property
    def cswv(self):
        return self._isol.get_cswv()

    @property
    def cswf(self):
        return self._isol.get_cswf()

    @property
    def cgmem(self):
        return self._isol.get_cgmem()

    @property
    def exitcode(self):
        return self._isol.get_exitcode()

    @property
    def stdout(self):
        return  self._isol.get_stdout()
