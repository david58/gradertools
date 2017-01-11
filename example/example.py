from gradertools import Compile
from gradertools import Execute
c = Compile('source.py')
c.compile()
bp = c.binarypath
e = Execute(bp)
e.execute()

c = Compile('source.cpp')
c.compile()
bp = c.binarypath
e = Execute(bp)
e.execute()
