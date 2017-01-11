from .compile_python import CompilerPython
from .compile_cpp import CompilerCpp


class Compile:
    def __init__(self, sourcepath):
        extension = sourcepath.split('.')[-1]

        if extension == 'py':
            Compiler = CompilerPython
        elif extension == 'cpp':
            Compiler = CompilerCpp
        else:
            raise Exception('Unknown Language')

        self._comp = Compiler(sourcepath)
        
    @property
    def binarypath(self):
        return self._comp.get_binarypath()

    def compile(self):
        self._comp.compile()
