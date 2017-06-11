import shutil
import os
from .interface import VerificateInterface
from ..isolation.isolate import Isolate


class VerificateDiff(VerificateInterface):
    def verificate(self):

        infile = self.inputfile
        outfile = self.outputfile
        correctoutput = self.correctoutput

        isol = Isolate()
        command = '../progdiff/progdiff'
        args = [ os.path.basename(correctoutput),  os.path.basename(outfile), 'náš', 'tvoj']
        isol.isolate(files=['../progdiff/progdiff', outfile, correctoutput], command=command, parameters=args, stdoutfile='output.out')


        box=isol.boxdir
        self._message = open(os.path.join(box, 'output.out'), 'r').read()

        isol.clean()
