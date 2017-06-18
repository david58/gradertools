import os
from .execute_python import ExecutePython
from .execute_binary import ExecuteBinary


class Execute:
    def __init__(self, binarypath, inputfile, outputfile, executor, isolator=None):
        if executor == 'python':
            Executor = ExecutePython
        else:
            Executor = ExecuteBinary

        self._isol = isolator
        self._exec = Executor(binarypath, inputfile, outputfile)

    def execute(self):
        self._exec.execute(self._isol)

    @property
    def status(self):
        return self._exec.get_status()

    @property
    def time(self):
        return self._exec.get_time()
