import shutil
import os
from .interface import CompilerInterface
from ..isolation.isolate import Isolate


class CompilerCpp(CompilerInterface):
    def compile(self):
        sp = self.sourcepath
        isol = Isolate()
        command = '/usr/bin/g++'
        args = ['-static', '-std=gnu++14', '-O2', '-Wall', '-Wextra', '-ocompiledbinary', os.path.basename(sp)]
        envvars = ['PATH=/usr/bin']
        isol.isolate(files=[sp], command=command, parameters=args, envvariables=envvars, allowmultiprocess=True)
        if isol.status == 'OK':
            self._status = 'OK'
        elif isol.status == 'TO':
            self._status = 'CTLE'
        else:
            self._status = 'CE'
            out = str(isol.stdout, 'utf-8', errors='replace')
            if len(out) > 10000:
                self._error = out[:10000] + '\n\n(Compiler output too long, truncated.)\n'
            else:
                self._error = out
        if self._status == 'OK':
            box = isol.boxdir
            try:
                shutil.copy(os.path.join(box, 'compiledbinary'), 'compiledbinary')
                self._binarypath = 'compiledbinary'
            except:
                self._status = 'IN'
        isol.clean()
