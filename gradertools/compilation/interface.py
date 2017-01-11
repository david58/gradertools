class CompilerInterface:
    
    def __init__(self, sourcepath):
        self.sourcepath = sourcepath
        self._binarypath = None
    
    def compile(self):
        raise NotImplementedError
    
    def get_binarypath(self):
        return self._binarypath
