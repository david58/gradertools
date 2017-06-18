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

        for test_input in sorted(os.listdir(os.path.join(task,'test'))):
            if not (test_input.endswith('.in')):
                continue

            group = test_input[: test_input.index('.')]
            if group != lastgroup:
                lastgroup = group
            subgroup = vstup[vstup.index('.') + 1: -3]
            print(' ' + subgroup, end='')
            sys.stdout.flush()

            vystup = vstup[:-3] + '.out'
            batch = vstup.split('.')[0]
            if mode == testing_mode.BATCH and batch_results[batch] != 'OK' and vstup.count(
                    '.sample.') == 0 and vstup.count('.example.') == 0:
                # print( 'skipped (batch already failed)' )
                print(' skip ;', end='')
                sys.stdout.flush()
                all_tests_cfg.add_section(vstup)
                all_tests_cfg[vstup]['status'] = 'IG'
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