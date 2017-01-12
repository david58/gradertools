import subprocess
import shutil
import os
from .interface import ExecuteInterface


class ExecuteBinary(ExecuteInterface):
    def execute(self):
        bp = self.binarypath
        box = subprocess.run(['../isolate/isolate', '--init'], check=True, stdout=subprocess.PIPE).stdout
        box = str(box.strip(), 'utf-8', errors='ignore')
        shutil.copy(bp, os.path.join(box, 'box', 'binary'))
        out = subprocess.run(['../isolate/isolate', '--run', 'binary'],
                             check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(out.stdout)
        subprocess.run(['../isolate/isolate', '--cleanup'], check=True)
