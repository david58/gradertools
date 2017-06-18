import shutil
import os
import filecmp
from .interface import VerificateInterface


class VerificateDiff(VerificateInterface):
    def verificate(self,isol):

        outfile = self.outputfile
        correctoutput = self.correctoutput
        print(filecmp.cmp(outfile,correctoutput))
        if filecmp.cmp(outfile,correctoutput):
            self._status = 'OK'
        else:
            self._status = 'WA'
            command = './progdiff'
            args = [ os.path.basename(correctoutput),  os.path.basename(outfile), 'náš', 'tvoj']
            isol.isolate(files=['./progdiff-1.0/progdiff', outfile, correctoutput], command=command, parameters=args, stdoutfile='diffout.out')


            box=isol.boxdir
            self._message = open(os.path.join(box, 'diffout.out'), 'r').read()

            #isol.clean()
        filecmp.clear_cache()