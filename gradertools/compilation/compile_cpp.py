from .interface import CompilerInterface


class CompilerCpp(CompilerInterface):
    def compile(self):
        # TODO
        self._binarypath = 'compiledbinary'
        print("cpp")
