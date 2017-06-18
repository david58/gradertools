from .verificate_diff import VerificateDiff


class Verificate:
    def __init__(self,  inputfile, outputfile, correctoutput, isolator=None):
        Verificator = VerificateDiff
        self._verif = Verificator(inputfile, outputfile, correctoutput)
        self._isol = isolator

    def verificate(self):
        self._verif.verificate(self._isol)

    @property
    def status(self):
        return self._verif.get_status()

    @property
    def message(self):
        return self._verif.get_message()
