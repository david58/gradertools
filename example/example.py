from gradertools import Compile
from gradertools import Execute
print('python')
c = Compile('source.py')
c.compile()
print('compiled')
bp = c.binarypath
e = Execute(bp)
e.execute()
print('executed')

print('c++')
c = Compile('source.cpp')
c.compile()
print('compilation: '+c.status)
if c.status == 'OK':
    bp = c.binarypath
    e = Execute(bp)
    e.execute()
    print('execution: '+e.status)
