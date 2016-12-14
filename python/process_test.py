import os
import subprocess

print('pid :', os.getpid())
print('uid :', os.getuid())
print('gid :', os.getgid())
print()

print('date :', subprocess.getoutput('date'))
print('pwd :', subprocess.getoutput('pwd'))
print()

print('date result :', subprocess.call('date'))
