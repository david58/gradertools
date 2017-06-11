import argparse
from .compilation.compile import Compile
from .execution.execute import Execute
from .verification.verificate import Verificate

c = Compile('source.py')
c.compile()

if c.status == 'OK':
    bp = c.binarypath
    e = Execute(bp, 'input.in', 'output.out')
    e.execute()

if e.status =='OK':
    v = Verificate('input.in', 'output.out', 'correct.out')


