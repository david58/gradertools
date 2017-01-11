from .interface import CompilerInterface


class CompilerPython(CompilerInterface):
    def compile(self):
        self._binarypath = self.sourcepath
        print("python")
