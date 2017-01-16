class ExecuteInterface:
    def __init__(self, binarypath, inputfile, outputfile):
        self.binarypath = binarypath
        self.inputfile = inputfile
        self.outputfile = outputfile
        self._status = None

    def execute(self):
        raise NotImplementedError

    def get_status(self):
        return self._status
