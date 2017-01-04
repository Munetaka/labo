import subprocess
import sys

res = subprocess.run(["ls", "-l", "-a"], stdout=subprocess.PIPE)
out = res.stdout
# p = subprocess.Popen(["ls", "-l", "-a"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# out, err = p.communicate()
# print(out)
print([s for s in out.decode('utf8').split('\n') if s])
# sys.stdout.buffer.write(res.stdout)
