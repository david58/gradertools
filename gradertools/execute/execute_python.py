import subprocess
import shutil
import os
from .interface import ExecuteInterface


class ExecutePython(ExecuteInterface):
    def execute(self):
        bp = self.binarypath
        box = subprocess.run(['../isolate/isolate', '--init'], check=True, stdout=subprocess.PIPE).stdout
        box = str(box.strip(), 'utf-8', errors='ignore')
        shutil.copyfile(bp, os.path.join(box, 'box', 'source.py'))
        out = subprocess.run(['../isolate/isolate', '--env=PATH=/usr/bin', '--env=HOME=/', '--dir=/etc', '--run',
                              '/usr/bin/python3', 'source.py'],
                             check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(out.stdout)
        subprocess.run(['../isolate/isolate', '--cleanup'], check=True)
