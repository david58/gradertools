import os
from .interface import ExecuteInterface
from ..isolation.isolate import Isolate


class ExecuteBinary(ExecuteInterface):
    def execute(self):
        bp = self.binarypath
        isol = Isolate()
        command = './'+os.path.basename(bp)
        isol.isolate(files=[bp], command=command)
        if isol.status == 'OK':
            self._status = 'OK'
        elif isol.status == 'TO':
            self._status = 'TLE'
        elif isol.status == 'SG':
            self._status = 'EXC'
        elif isol.status == 'RE':
            self._status = 'EXC'
        else:
            self._status = 'IN'
        isol.clean()
