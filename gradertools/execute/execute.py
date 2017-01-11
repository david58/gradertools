from .execute_python import ExecutePython
from .execute_binary import ExecuteBinary


class Execute:
    def __init__(self, binarypath):
        extension = binarypath.split('.')[-1]

        if extension == 'py':
            Executor = ExecutePython
        else:
            Executor = ExecuteBinary

        self._exec = Executor(binarypath)

    def execute(self):
        self._exec.execute()
