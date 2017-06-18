import os
from .compile_python import CompilerPython
from .compile_cpp import CompilerCpp
#from ..isolation.isolate import Isolate


class Compile:
    def __init__(self, sourcepath, compiler, isolator=None):
        if compiler == 'python':
            Compiler = CompilerPython
        elif compiler == 'cpp':
            Compiler = CompilerCpp
        else:
            raise Exception('Unknown Language')
#        if isolator is None:
#            self._isol = Isolate()
#        else:
        self._isol = isolator

        self._comp = Compiler(sourcepath)
        
    @property
    def binarypath(self):
        return self._comp.get_binarypath()

    @property
    def status(self):
        return self._comp.get_status()

    @property
    def errormessage(self):
        return self._comp.get_error()

    def compile(self):
        self._comp.compile(self._isol)
