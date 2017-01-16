import os
from .compile_python import CompilerPython
from .compile_cpp import CompilerCpp


class Compile:
    def __init__(self, sourcepath):
        extension = os.path.splitext(sourcepath)[-1]

        if extension == '.py':
            Compiler = CompilerPython
        elif extension == '.cpp':
            Compiler = CompilerCpp
        else:
            raise Exception('Unknown Language')

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
        self._comp.compile()
