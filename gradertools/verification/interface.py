class VerificateInterface:
    def __init__(self, inputfile, outputfile, correctoutput):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.correctoutput = correctoutput
        self._status = None
        self._message = None

    def verificate(self):
        raise NotImplementedError

    def get_status(self):
        return self._status

    def get_message(self):
        return self._message