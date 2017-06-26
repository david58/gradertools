class Command:
    def __init__(self, binary, args=[], input=None, output=None, wait=False):
        self.commands = []
        self.commands.append({
            'execute':binary,
            'args':args,
            'input':input,
            'output':output,
            'wait':wait,
        })
        self._files = []
        self._envvariables = []
        self._directories = []
        self._allowmultiprocess = False

    def set_multiprocess(self, multiprocess):
        self._allowmultiprocess = multiprocess

#    def add_command(self,):

#    def execute(self,isolator, timelimit, memlimit, ):

#        return isolator.isolate(self._files, command, parameters, envvariables, directories, allowmultiprocess, stdinfile,
#                                  stdoutfile)