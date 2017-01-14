import shutil
import os
from .interface import CompilerInterface
from ..isolation.isolate import Isolate


class CompilerCpp(CompilerInterface):
    def compile(self):
        sp = self.sourcepath
        isol = Isolate()
        command = '/usr/bin/g++'
        args = ['-ocompiledbinary', os.path.basename(sp)]
        envvars = ['PATH=/usr/bin', 'HOME=/']
        (box, out, err) = isol.isolate(files=[sp], command=command, parameters=args, envvariables=envvars, allowmultiprocess=True)
        shutil.copy(os.path.join(box, 'compiledbinary'), 'compiledbinary')
        self._binarypath = 'compiledbinary'
        isol.clean()
