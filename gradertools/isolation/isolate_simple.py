import subprocess
import shutil
import os
import time
from .interface import IsolateInterface


class IsolateSimple(IsolateInterface):

    def isolate(self, files, command, parameters, envvariables, directories, allowmultiprocess, stdinfile, stdoutfile):
        if os.path.isdir("/tmp/gradertools/isolation/"):
            shutil.rmtree("/tmp/gradertools/isolation/")
        os.makedirs("/tmp/gradertools/isolation/")
        box = "/tmp/gradertools/isolation/"
        for file in files:
            shutil.copy(file, os.path.join(box, os.path.basename(file)))
        isolateio=" "
        if stdinfile is not None:
            isolateio+="< "+stdinfile

        if stdoutfile is not None:
            isolateio+="> "+stdoutfile

        t0 = time.perf_counter()
        out = subprocess.run(" ".join(["cd "+ box+ ";"]+[command]+parameters+[isolateio]), shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        t1 = time.perf_counter()
        self._boxdir = box
        self._status = 'OK'
        self._runtime = t1-t0
        self._walltime = t1-t0
        self._maxrss = 0        # Maximum resident set size of the process (in kilobytes).
        self._cswv = 0    # Number of context switches caused by the process giving up the CPU voluntarily.
        self._cswf = 0       # Number of context switches forced by the kernel.
        self._cgmem = 0          # Total memory use by the whole control group (in kilobytes).
        self._exitcode = out.returncode
        self._stdout = out.stdout

    def clean(self):
        shutil.rmtree("/tmp/gradertools/isolation/")
