import os
from .interface import ExecuteInterface
from ..isolation.isolate import Isolate


class ExecuteBinary(ExecuteInterface):
    def execute(self):
        bp = self.binarypath
        isol = Isolate()
        command = './'+os.path.basename(bp)
        (box, out, err) = isol.isolate(files=[bp], command=command)
        print(out)
        isol.clean()
