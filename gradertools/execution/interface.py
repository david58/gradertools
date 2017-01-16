class ExecuteInterface:
    def __init__(self, binarypath):
        self.binarypath = binarypath
        self._status = None

    def execute(self):
        raise NotImplementedError

    def get_status(self):
        return self._status
