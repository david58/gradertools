import os
from .interface import ExecuteInterface
from ..isolation.isolate import Isolate


class ExecutePython(ExecuteInterface):
    def execute(self):
        bp = self.binarypath
        isol = Isolate()
        command = '/usr/bin/python3'
        args = [os.path.basename(bp)]
        envvars = ['PATH=/usr/bin', 'HOME=/box']
        dirs = ['/etc']
        isol.isolate(files=[bp], command=command, parameters=args, envvariables=envvars, directories=dirs)
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
