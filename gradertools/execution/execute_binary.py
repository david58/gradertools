import shutil
import os
from .interface import ExecuteInterface
from ..isolation.isolate import Isolate


class ExecuteBinary(ExecuteInterface):
    def execute(self):
        bp = self.binarypath
        infile = self.inputfile
        outfile = self.outputfile
        isol = Isolate()
        command = './'+os.path.basename(bp)
        isol.isolate(files=[bp, infile], command=command, stdinfile=os.path.basename(infile), stdoutfile='output.out')

        self._status = 'OK'
        if isol.status == 'TO':
            self._status = 'TLE'
        elif isol.status == 'SG':
            self._status = 'EXC'
        elif isol.status == 'RE':
            self._status = 'EXC'
        elif isol.status == 'XX':
            self._status = 'IN'

        if self._status == 'OK':
            box=isol.boxdir
            try:
                shutil.copy(os.path.join(box, 'output.out'), outfile)
            except:
                self._status = 'IN'
        isol.clean()
