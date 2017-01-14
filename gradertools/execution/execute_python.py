import subprocess
import shutil
import os
from .interface import ExecuteInterface
from ..isolation.isolate import Isolate


class ExecutePython(ExecuteInterface):
    def execute(self):
        bp = self.binarypath
        isol = Isolate()
        command = '/usr/bin/python3'
        args=[os.path.basename(bp)]
        envvars=['PATH=/usr/bin', 'HOME=/']
        dirs=['/etc']
        (box, out, err) = isol.isolate(files=[bp], command=command, parameters=args, envvariables=envvars, directories=dirs)
        print(out)
        isol.clean()
