import subprocess
import shutil
import os
from .interface import CompilerInterface


class CompilerCpp(CompilerInterface):
    def compile(self):
        sp = self.sourcepath
        box = subprocess.run(['../isolate/isolate', '--init'], check=True, stdout=subprocess.PIPE).stdout
        box = str(box.strip(), 'utf-8', errors='ignore')
        shutil.copyfile(sp, os.path.join(box, 'box', 'source.cpp'))
        out = subprocess.run(['../isolate/isolate', '--env=PATH=/usr/bin', '--processes', '--dir=/etc', '--run',
                              '--',
                              '/usr/bin/g++', '-o', 'compiledbinary', 'source.cpp'],
                             check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        shutil.copy(os.path.join(box, 'box', 'compiledbinary'), 'compiledbinary')
        self._binarypath = 'compiledbinary'
        subprocess.run(['../isolate/isolate', '--cleanup'], check=True)
        print('c++')
