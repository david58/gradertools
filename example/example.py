from gradertools import Compile
from gradertools import Execute
print('python')
c = Compile('source.py')
c.compile()
print('compilation: ' + c.status)
if c.status == 'OK':
    bp = c.binarypath
    e = Execute(bp, 'input.in', 'outpy.out')
    e.execute()
    print('execution:', e.status, 'time:', e.time)
elif c.status == 'CE':
    print(c.errormessage)

print('c++')
c = Compile('source.cpp')
c.compile()
print('compilation: ' + c.status)
if c.status == 'OK':
    bp = c.binarypath
    e = Execute(bp, 'input.in', 'outcpp.out')
    e.execute()
    print('execution:', e.status, 'time:', e.time)
elif c.status == 'CE':
    print(c.errormessage)
