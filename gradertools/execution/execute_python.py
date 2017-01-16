import os
import shutil
from .interface import ExecuteInterface
from ..isolation.isolate import Isolate


class ExecutePython(ExecuteInterface):
    def execute(self):
        bp = self.binarypath
        infile = self.inputfile
        outfile = self.outputfile
        isol = Isolate()
        command = '/usr/bin/python3'
        args = [os.path.basename(bp)]
        envvars = ['PATH=/usr/bin', 'HOME=/box']
        dirs = ['/etc']
        isol.isolate(files=[bp, infile], command=command, parameters=args, envvariables=envvars, directories=dirs,
                     stdinfile=os.path.basename(infile), stdoutfile='output.out')
        self._time = isol.time
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
            box = isol.boxdir
            try:
                shutil.copy(os.path.join(box, 'output.out'), outfile)
            except:
                self._status = 'IN'
        isol.clean()
