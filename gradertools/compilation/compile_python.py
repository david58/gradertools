import os
from .interface import CompilerInterface


class CompilerPython(CompilerInterface):
    def compile(self, isol):
        self._binarypath = self.sourcepath
        sp = self.sourcepath
        command = '/usr/bin/python3'
        args = ['-m', 'py_compile', os.path.basename(sp)]
        envvars = ['PATH=/usr/bin', 'HOME=/box']
        isol.isolate(files=[sp], command=command, parameters=args, envvariables=envvars, allowmultiprocess=True)

        self._status = isol.status
        out = str(isol.stdout, 'utf-8', errors='replace')
        if len(out) > 10000:
            self._error = out[:10000] + '\n\n(Compiler output too long, truncated.)\n'
        else:
            self._error = out
        isol.clean()
