#!/usr/bin/env python

from compilation.compile import Compile
from execution.execute import Execute
from verification.verificate import Verificate
from isolation.isolate import Isolate
import sys
import os


#if e.status =='OK':
#    v = Verificate('input.in', 'output.out', 'correct.out')

if __name__ == "__main__":
    task=sys.argv[1]
    code=sys.argv[2]

    i = Isolate(isolator='simple')
    c = Compile(code, 'cpp', i)
    c.compile()
    if c.status!='OK':
        print(c.errormessage)
    else:
        print('Compilation successful')
        bp = c.binarypath

# temorary
        from collections import defaultdict
        batch_results = defaultdict(lambda: 'OK')

        for test_input in sorted(os.listdir(os.path.join(task,'test'))):
            if not (test_input.endswith('.in')):
                continue

            vystup = test_input[:-3] + '.out'
            batch = test_input.split('.')[0]
            if batch_results[batch] != 'OK' and test_input.count(
                    '.sample.') == 0 and test_input.count('.example.') == 0:
                status = 'IG'
                continue



        e = Execute(bp, os.path.join(task,"test", "01.in"), "output.out", "cpp",i)
        e.execute()
        status=e.status
        if e.status=='OK':
            v = Verificate(os.path.join(task,"test", "01.in"), os.path.join(task,"test", "01.out"), "output.out",i)
            v.verificate()
            status=v.status
        print(status, str(int(e.time*1000))+'ms')
        if status == 'WA':
            print(v.message)
        os.remove("compiledbinary")