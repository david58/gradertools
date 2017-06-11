class ExecuteInterface:
    def __init__(self, binarypath, inputfile, outputfile):
        self.binarypath = binarypath
        self.inputfile = inputfile
        self.outputfile = outputfile
        self._status = None
        self._time = None

    def execute(self):
        raise NotImplementedError

    def get_status(self):
        return self._status

    def get_time(self):
        return self._time
