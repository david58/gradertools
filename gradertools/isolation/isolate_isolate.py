import subprocess
import shutil
import os
from .interface import IsolateInterface


class IsolateIsolate(IsolateInterface):

    def isolate(self, files, command, parameters, envvariables, directories, allowmultiprocess):
        box = subprocess.run(['../isolate/isolate', '--init'], check=True, stdout=subprocess.PIPE).stdout
        box = str(box.strip(), 'utf-8', errors='ignore')
        for file in files:
            shutil.copy(file, os.path.join(box, 'box', os.path.basename(file)))
        isolate_args = []
        for ev in envvariables:
            isolate_args.append('--env=' + ev)
        for dir in directories:
            isolate_args.append('--dir=' + dir)
        if allowmultiprocess:
            isolate_args.append('--processes')
        #print(['../isolate/isolate', '--env=PATH=/usr/bin']+isolate_args+['--run', '--']+[command]+parameters)
        out = subprocess.run(['../isolate/isolate']+isolate_args+['--run', '--']+[command]+parameters,
                             check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return os.path.join(box, 'box'), out.stdout, out.stderr

    def clean(self):
        subprocess.run(['../isolate/isolate', '--cleanup'], check=True)
