import shutil
import os
from .interface import ExecuteInterface


class ExecuteBinary(ExecuteInterface):
    def execute(self, isol):
        bp = self.binarypath
        infile = self.inputfile
        outfile = self.outputfile
        command = './'+os.path.basename(bp)
        isol.isolate(files=[bp, infile], command=command, stdinfile=os.path.basename(infile), stdoutfile='output.out')
        self._time = isol.time
        self._status = isol.status

        if self._status == 'OK':
            box = isol.boxdir
            try:
                shutil.copy(os.path.join(box, 'output.out'), outfile)
            except:
                self._status = 'IN'
        isol.clean()
