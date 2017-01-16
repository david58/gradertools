class IsolateInterface:
    def __init__(self, isolator):
        self.isolator = isolator
        self._status = None
        self._boxdir = None
        self._runtime = None
        self._walltime = None
        self._maxrss = None
        self._cswv = None
        self._cswf = None
        self._cgmem = None
        self._stdout = None
        self._exitcode = None

    def isolate(self, files, command, parameters, envvariables, directories, allowmultiprocess, stdinfile, stdoutfile):
        raise NotImplementedError

    def clean(self):
        raise NotImplementedError

    def get_status(self):
        return self._status

    def get_boxdir(self):
        return self._boxdir

    def get_time(self):
        return self._runtime

    def get_walltime(self):
        return self._walltime

    def get_maxrss(self):
        return self._maxrss

    def get_cswf(self):
        return self._cswf

    def get_cswv(self):
        return self._cswv

    def get_cgmem(self):
        return self._cgmem

    def get_stdout(self):
        return self._stdout

    def get_exitcode(self):
        return self._exitcode
