import os
from .interface import CompilerInterface
from ..isolation.isolate import Isolate


class CompilerPython(CompilerInterface):
    def compile(self):
        self._binarypath = self.sourcepath
        sp = self.sourcepath
        isol = Isolate()
        command = '/usr/bin/python3'
        args = ['-m', 'py_compile', os.path.basename(sp)]
        envvars = ['PATH=/usr/bin', 'HOME=/box']
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
        isol.clean()