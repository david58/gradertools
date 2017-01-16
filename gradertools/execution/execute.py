import os
from .execute_python import ExecutePython
from .execute_binary import ExecuteBinary


class Execute:
    def __init__(self, binarypath):
        extension = os.path.splitext(binarypath)[-1]

        if extension == 'py':
            Executor = ExecutePython
        else:
            Executor = ExecuteBinary

        self._exec = Executor(binarypath)

    def execute(self):
        self._exec.execute()

    @property
    def status(self):
        return self._exec.get_status()
