import os
import shutil
from .interface import ExecuteInterface


class ExecutePython(ExecuteInterface):
    def execute(self, isol):
        bp = self.binarypath
        infile = self.inputfile
        outfile = self.outputfile
        command = '/usr/bin/python3'
        args = [os.path.basename(bp)]
        envvars = ['PATH=/usr/bin', 'HOME=/box']
        dirs = ['/etc']
        isol.isolate(
            files=[bp, infile], command=command, parameters=args, envvariables=envvars, directories=dirs,
            stdinfile=os.path.basename(infile), stdoutfile='output.out'
        )
        self._time = isol.time
        self._status = isol.status

        if self._status == 'OK':
            box = isol.boxdir
            try:
                shutil.copy(os.path.join(box, 'output.out'), outfile)
            except:
                self._status = 'IN'
        #isol.clean()
