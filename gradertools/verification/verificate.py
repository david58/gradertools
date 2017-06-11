from .verificate_diff import VerificateDiff


class Verificate:
    def __init__(self,  inputfile, outputfile, correctoutput):
        Verificator = VerificateDiff
        self._verif = Verificator(inputfile, outputfile, correctoutput)

    def verificate(self):
        self._verif.verificate()

    @property
    def status(self):
        return self._verif.get_status()

    @property
    def message(self):
        return self._verif.get_message()
