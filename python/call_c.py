import subprocess
import os


def main():
    c_file = 'countup.c'
    values = range(0, 20, 2)
    array_str = '{ %s }' % (' '.join(map(lambda s: '%d,' % s, values)))[:-1]
    test_c_format = """
#include<stdio.h>

int main() {
  int n = %d;
  int s_size[] = %s;
  int i;

  for (i = 0; i < n; i++) {
    printf("%%d\\n", s_size[i]);
  }
}
"""
    with open(c_file, 'w') as f:
        f.write(test_c_format % (len(values), array_str))

    os.system("gcc %s" % c_file)
    result = subprocess.Popen('./a.out', stdout=subprocess.PIPE).communicate()[0]

    for i, v in enumerate(result.decode('utf8')[:-1].split('\n')):
        print(i, v)

if __name__ == '__main__':
    main()
