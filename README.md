# gradertools

## Download
```bash
$git clone --recursive https://github.com/david58/gradertools.git
```
Or run this command after non-recursive clone for isolate submodule
```bash
$git submodule update --init
```

## Install
Inside isolate folder run
```bash
$make isolate
```
## Run
Need to by run as root.

Open in pycharm and execute example.py.

testovac@foja:~/tasks$ grep  "task" ./**/metadata.config |wc -l
1745
testovac@foja:~/tasks$ grep  "tester" ./**/metadata.config |wc -l
304
testovac@foja:~/tasks$ grep "custom_execute" ./**/metadata.config |wc -l
38
testovac@foja:~/tasks$ grep "custom_compile" ./**/metadata.config |wc -l
5
