class CompilerInterface:
    
    def __init__(self, sourcepath):
        self.sourcepath = sourcepath
        self._binarypath = None
        self._status = None
    
    def compile(self):
        raise NotImplementedError
    
    def get_binarypath(self):
        return self._binarypath

    def get_status(self):
        return self._status
