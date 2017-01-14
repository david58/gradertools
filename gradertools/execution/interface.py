class ExecuteInterface:
    def __init__(self, binarypath):
        self.binarypath = binarypath

    def execute(self):
        raise NotImplementedError
