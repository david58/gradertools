import subprocess
import shutil
import os
import configparser
from .interface import IsolateInterface


class IsolateIsolate(IsolateInterface):

    def isolate(self, files, command, parameters, envvariables, directories, allowmultiprocess, stdinfile, stdoutfile):
        out = subprocess.run(['../isolate/isolate', '--cg', '--init'], stdout=subprocess.PIPE)
        if out.returncode != 0:
            self._status = 'IN'
        box = out.stdout
        box = str(box.strip(), 'utf-8', errors='ignore')
        for file in files:
            shutil.copy(file, os.path.join(box, 'box', os.path.basename(file)))
        isolate_args = []
        for ev in envvariables:
            isolate_args.append('--env=' + ev)
        for d in directories:
            isolate_args.append('--dir=' + d)
        if allowmultiprocess:
            isolate_args.append('--processes')
        if stdinfile is not None:
            isolate_args.append('--stdin='+stdinfile)
        if stdoutfile is not None:
            isolate_args.append('--stdout='+stdoutfile)
        out = subprocess.run(['../isolate/isolate', '--cg', '--cg-timing', '--meta=isolate.meta'] + isolate_args
                             + ['--run', '--']+[command]+parameters,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        with open('isolate.meta', 'r') as f:
            config_string = '[section]\n' + f.read()
        config = configparser.ConfigParser()
        config.read_string(config_string)
        # print(config_string)
        self._boxdir = os.path.join(box, 'box')
        self._status = config.get('section', 'status', fallback='OK')
        self._runtime = config.getfloat('section', 'time', fallback=0)
        self._walltime = config.getfloat('section', 'time-wall', fallback=0)
        self._maxrss = config.getint('section', 'max-rss', fallback=0)        # Maximum resident set size of the process (in kilobytes).
        self._cswv = config.getint('section', 'csw-voluntary', fallback=0)    # Number of context switches caused by the process giving up the CPU voluntarily.
        self._cswf = config.getint('section', 'csw-forced', fallback=0)       # Number of context switches forced by the kernel.
        self._cgmem = config.getint('section', 'cg-mem', fallback=0)          # Total memory use by the whole control group (in kilobytes).
        self._exitcode = config.getint('section', 'exitcode', fallback=0)
        self._stdout = out.stdout

    def clean(self):
        subprocess.run(['../isolate/isolate', '--cg', '--cleanup'])
